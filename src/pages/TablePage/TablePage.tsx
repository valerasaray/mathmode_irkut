import {
  TableContainer,
  Table,
  TableBody,
  TableHead,
  TableCell,
  TableRow,
  Stack,
  TextField,
  TablePagination,
} from "@mui/material";
import { ITable } from "../../models/tableModels/ITable";
import { useState, useMemo, useEffect } from "react";
import { TableFabric } from "../../components/TableFabric/TableFabric";
import { TableToolTip } from "../../components/TableModules";
import { TableColumns } from "../../components/TableFabric/Tables/TableColumns/TableColumns";
import { CreateProcessModal } from "../../components/Modals/CreateProcessModal/CreateProcessModal";
import {
  IFilter,
  setFilters,
} from "../../redux/reducers/filterReducer/filterReducer";
import { useDispatch } from "react-redux";
import { getProcedures } from "../../api/tableApi/getProcedures";
import { ISearchProcess } from "../../models/tableModels/ISearchProcess";
import { useSelector } from "react-redux";
import { RootState } from "../../redux/store";
import { ProjectCard } from "../../components/ProjectCard/ProjectCard";

const defaultFilters: IFilter = {
  procedureType: ["ИИ"],
  department: ["Отделение планера"],
  matcher: ["Петров В.И.", "Петров В.В."],
};

const defaultSearch: ISearchProcess = {
  department: "",
  matcher: "",
  procedureType: "",
};

export const TablePage = () => {
  const [table, setTable] = useState<ITable[]>([]);
  const [filteredTable, setFilteredTable] = useState<ITable[]>([]);
  const [rowsPerPage, setRowsPerPage] = useState<number>(5);
  const [page, setPage] = useState<number>(0);
  const [searchData, setSearchData] = useState<ISearchProcess>(defaultSearch);
  const [isZoomable, setIsZoomable] = useState<number>(0);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const userData = useSelector((state: RootState) => state.userInfo.userInfo);

  const dispatch = useDispatch();

  useEffect(() => {
    setIsLoading(true);
    getProcedures(
      userData.login,
      (value) => {
        setTable(value);
        setFilteredTable(value);
      },
      undefined,
      false
    ).then(() => {
      setIsLoading(false);
    });
    dispatch(setFilters(defaultFilters));
  }, [table]);

  useEffect(() => {
    setFilteredTable(
      table.filter(
        (row) =>
          row.realiser.login.includes(searchData.matcher) &&
          row.processType.value.includes(searchData.procedureType) &&
          row.realiserGroup.title.includes(searchData.department)
      )
    );
  }, [searchData]);

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  if (isLoading) {
    return <></>;
  }

  const getTableByToolTip = (pageNumber: number) => {
    switch (pageNumber) {
      case 0:
        return (
          <>
            <TableContainer>
              <Table aria-label="collapsible table">
                <TableHead>
                  <TableRow>
                    <TableCell colSpan={4}></TableCell>
                    <TableColumns rowMatching={table[0]} isPhase />
                  </TableRow>
                  <TableRow>
                    <TableCell>Наименования паспорта</TableCell>
                    <TableCell align="right">Выпускающий</TableCell>
                    <TableCell align="right">
                      Подразделение выпускающего
                    </TableCell>
                    <TableCell align="right">Тип процедуры выпуска</TableCell>
                    <TableColumns rowMatching={table[0]} isPhase={false} />
                  </TableRow>
                </TableHead>
                <TableBody>
                  {filteredTable &&
                    (filteredTable.length === 0 ? table : filteredTable)
                      .slice(
                        page * rowsPerPage,
                        page * rowsPerPage + rowsPerPage
                      )
                      .map((row, index) => (
                        <TableFabric
                          key={index}
                          rowMatching={row}
                          isZoomable={isZoomable}
                          isMatching={
                            userData?.rights
                              ? userData?.rights.length === 0
                              : true
                          }
                        />
                      ))}
                </TableBody>
              </Table>
            </TableContainer>
            <TablePagination
              rowsPerPageOptions={[5, 10, 25]}
              labelRowsPerPage={"Строк на странице"}
              component="div"
              count={table.length}
              rowsPerPage={rowsPerPage}
              page={page}
              onPageChange={handleChangePage}
              onRowsPerPageChange={handleChangeRowsPerPage}
            />
          </>
        );
      case 1:
        return (
          <>
            {" "}
            <TableContainer>
              <Table aria-label="collapsible table">
                <TableHead>
                  <TableRow>
                    <TableCell />
                    <TableCell>Наименования паспорта</TableCell>
                    <TableCell align="right">Выпускающий</TableCell>
                    <TableCell align="right">
                      Подразделение выпускающего
                    </TableCell>
                    <TableCell align="right">Тип процедуры выпуска</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {filteredTable &&
                    (filteredTable.length === 0 ? table : filteredTable)
                      .slice(
                        page * rowsPerPage,
                        page * rowsPerPage + rowsPerPage
                      )
                      .map((row, index) => (
                        <TableFabric
                          rowMatching={row}
                          key={index}
                          isZoomable={isZoomable}
                          isMatching={
                            userData?.rights
                              ? userData?.rights.length === 0
                              : true
                          }
                        />
                      ))}
                </TableBody>
              </Table>
              <TablePagination
                rowsPerPageOptions={[5, 10, 25]}
                labelRowsPerPage={"Строк на странице"}
                component="div"
                count={filteredTable.length}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
              />
            </TableContainer>
          </>
        );
      case 2:
        return (
          <Stack direction={"row"} flexWrap={"wrap"} gap={5}>
            {filteredTable &&
              (filteredTable.length === 0 ? table : filteredTable)
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((project, index) => (
                  <ProjectCard rowMatching={project} key={index} />
                ))}
          </Stack>
        );
    }
  };

  return (
    <Stack direction={"column"} padding={5}>
      <TableToolTip
        setIsZoomable={setIsZoomable}
        searchData={searchData}
        setSearchData={setSearchData}
      />
      {getTableByToolTip(isZoomable)}
      <CreateProcessModal />
    </Stack>
  );
};
