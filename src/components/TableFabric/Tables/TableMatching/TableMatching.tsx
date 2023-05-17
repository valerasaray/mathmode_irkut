import { FC, useState } from "react";
import { ITable } from "../../../../models/tableModels/ITable";
import {
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  IconButton,
  Collapse,
  Box,
  Typography,
} from "@mui/material";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import dayjs from "dayjs";

interface ITableMatchingProps {
  isZoomable: number;
  rowMatching: ITable;
}

export const TableMatching: FC<ITableMatchingProps> = ({
  isZoomable,
  rowMatching,
}) => {
  const [open, setOpen] = useState<boolean>(false);

  switch (isZoomable) {
    case 0:
      return (
        <TableRow>
          <TableCell component={"th"} scope={"row"}>
            {rowMatching?.passport_ref ?? ""}
          </TableCell>
          <TableCell align={"right"}>
            {rowMatching?.realiser?.login ?? ""}
          </TableCell>
          <TableCell align={"right"}>
            {rowMatching?.realiserGroup?.title ?? ""}
          </TableCell>
          <TableCell align={"right"}>
            {rowMatching?.processType?.value ?? ""}
          </TableCell>
          {rowMatching?.nodes &&
            rowMatching?.nodes.map((phase) => (
              <>
                <TableCell component="th" scope="row">
                  {phase?.subs ? phase?.subs[0].fit.FIO : ""}
                </TableCell>
                <TableCell>
                  {" "}
                  {dayjs(phase?.receipt).isValid()
                    ? dayjs(phase?.receipt).format("D MMMM YYYY")
                    : ""}
                </TableCell>
                <TableCell align="right">
                  {dayjs(
                    phase?.subs ? phase?.subs[0].start_verification : ""
                  ).isValid()
                    ? dayjs(
                        phase?.subs ? phase?.subs[0].start_verification : ""
                      ).format("D MMMM YYYY")
                    : ""}
                </TableCell>
                <TableCell align="right">
                  {phase?.addenable ? "Да" : "Нет"}
                </TableCell>
                <TableCell align="right">
                  {dayjs(
                    phase?.subs ? phase?.subs[0].end_verification : ""
                  ).isValid()
                    ? dayjs(
                        phase?.subs ? phase?.subs[0].end_verification : ""
                      ).format("D MMMM YYYY")
                    : ""}
                </TableCell>
                <TableCell align="right">
                  {dayjs(
                    phase?.subs ? phase?.subs[0].end_correction : ""
                  ).isValid()
                    ? dayjs(
                        phase?.subs ? phase?.subs[0].end_correction : ""
                      ).format("D MMMM YYYY")
                    : ""}
                </TableCell>
              </>
            ))}
        </TableRow>
      );
    case 1:
      return (
        <>
          <TableRow sx={{ "& > *": { borderBottom: "unset" } }}>
            <TableCell>
              <IconButton
                aria-label="expand row"
                size="small"
                onClick={() => setOpen(!open)}
              >
                {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
              </IconButton>
            </TableCell>
            <TableCell component={"th"} scope={"row"}>
              {rowMatching?.passport_ref ?? ""}
            </TableCell>
            <TableCell align={"right"}>
              {rowMatching?.realiser?.login ?? ""}
            </TableCell>
            <TableCell align={"right"}>
              {rowMatching?.realiserGroup?.title ?? ""}
            </TableCell>
            <TableCell align={"right"}>
              {rowMatching?.processType?.value ?? ""}
            </TableCell>
          </TableRow>
          {rowMatching?.nodes &&
            rowMatching?.nodes.map((phase, index) => (
              <TableRow>
                <TableCell
                  style={{ paddingBottom: 0, paddingTop: 0 }}
                  colSpan={10}
                  key={index}
                >
                  <Collapse in={open} timeout="auto" unmountOnExit>
                    <Box sx={{ margin: 1 }}>
                      <Typography variant="h6" gutterBottom component="div">
                        {phase.title}
                      </Typography>
                      <Table size="small" aria-label="purchases">
                        <TableHead>
                          <TableRow>
                            <TableCell>Фамилия согласующего</TableCell>
                            <TableCell>Дата поступления документа</TableCell>
                            <TableCell align="right">
                              Дата проверки документа
                            </TableCell>
                            <TableCell align="right">
                              Наличие замечаний
                            </TableCell>
                            <TableCell align="right">
                              Дата согласования
                            </TableCell>
                            <TableCell align="right">Дата подписания</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          <TableRow>
                            <TableCell component="th" scope="row">
                              {phase?.subs ? phase?.subs[0].fit.FIO : ""}
                            </TableCell>
                            <TableCell>
                              {" "}
                              {dayjs(phase?.receipt).isValid()
                                ? dayjs(phase?.receipt).format("D MMMM YYYY")
                                : ""}
                            </TableCell>
                            <TableCell align="right">
                              {dayjs(
                                phase?.subs
                                  ? phase?.subs[0].start_verification
                                  : ""
                              ).isValid()
                                ? dayjs(
                                    phase?.subs
                                      ? phase?.subs[0].start_verification
                                      : ""
                                  ).format("D MMMM YYYY")
                                : ""}
                            </TableCell>
                            <TableCell align="right">
                              {phase?.addenable ? "Да" : "Нет"}
                            </TableCell>
                            <TableCell align="right">
                              {dayjs(
                                phase?.subs
                                  ? phase?.subs[0].end_verification
                                  : ""
                              ).isValid()
                                ? dayjs(
                                    phase?.subs
                                      ? phase?.subs[0].end_verification
                                      : ""
                                  ).format("D MMMM YYYY")
                                : ""}
                            </TableCell>
                            <TableCell align="right">
                              {dayjs(
                                phase?.subs ? phase?.subs[0].end_correction : ""
                              ).isValid()
                                ? dayjs(
                                    phase?.subs
                                      ? phase?.subs[0].end_correction
                                      : ""
                                  ).format("D MMMM YYYY")
                                : ""}
                            </TableCell>
                          </TableRow>
                        </TableBody>
                      </Table>
                    </Box>
                  </Collapse>
                </TableCell>
              </TableRow>
            ))}
        </>
      );
    case 2:
      return <></>;
  }
};
