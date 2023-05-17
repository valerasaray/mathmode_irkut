import {
  Tooltip,
  Tabs,
  Tab,
  Stack,
  Button,
  Autocomplete,
  TextField,
} from "@mui/material";
import AutoAwesomeMosaicIcon from "@mui/icons-material/AutoAwesomeMosaic";
import AspectRatioIcon from "@mui/icons-material/AspectRatio";
import AppsIcon from "@mui/icons-material/Apps";
import { useState, Dispatch, SetStateAction, FC } from "react";
import { useDispatch } from "react-redux";
import { setModalActive } from "../../../redux/reducers/modalReducer/modalReducer";
import { useSelector } from "react-redux";
import { RootState } from "../../../redux/store";
import { ISearchProcess } from "../../../models/tableModels/ISearchProcess";

interface ITableToolTipProps {
  setIsZoomable: Dispatch<SetStateAction<number>>;
  searchData: ISearchProcess;
  setSearchData: Dispatch<SetStateAction<ISearchProcess>>;
}

export const TableToolTip: FC<ITableToolTipProps> = ({
  setIsZoomable,
  searchData,
  setSearchData,
}) => {
  const [value, setValue] = useState<number>(0);

  const filters = useSelector((state: RootState) => state.filter.filters);

  const dispatch = useDispatch();

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
    setIsZoomable(newValue);
  };
  return (
    <Stack direction={"column"} gap={2}>
      <Stack
        direction={"row"}
        gap={5}
        sx={{ alignItems: "center", justifyContent: "space-between" }}
      >
        <Button
          variant={"outlined"}
          onClick={() => dispatch(setModalActive("createProcessModal"))}
        >
          Создать процесс
        </Button>
        <Tabs value={value} onChange={handleChange}>
          <Tab
            label={
              <Tooltip title={"Обычная таблица"}>
                <AspectRatioIcon />
              </Tooltip>
            }
          ></Tab>
          <Tab
            label={
              <Tooltip title={"Книжный вариант"}>
                <AutoAwesomeMosaicIcon />
              </Tooltip>
            }
          ></Tab>
          <Tab
            label={
              <Tooltip title={"Графовый вариант"}>
                <AppsIcon />
              </Tooltip>
            }
          ></Tab>
        </Tabs>
      </Stack>
      <Stack direction={"row"} gap={5} sx={{ alignItems: "center" }}>
        <Autocomplete
          freeSolo
          disableClearable
          options={filters.matcher.map((item) => item)}
          fullWidth
          value={searchData?.matcher ?? ""}
          renderInput={(params) => (
            <TextField
              placeholder={"Выпускающий"}
              {...params}
              InputProps={{ ...params.InputProps, type: "search" }}
              onChange={(e) =>
                setSearchData({ ...searchData, matcher: e.target.value })
              }
            />
          )}
          onChange={(e: any, value: string) =>
            setSearchData({ ...searchData, matcher: value })
          }
        />
        <Autocomplete
          freeSolo
          disableClearable
          options={filters.procedureType.map((item) => item)}
          fullWidth
          value={searchData?.procedureType ?? ""}
          renderInput={(params) => (
            <TextField
              placeholder={"Тип документа"}
              {...params}
              InputProps={{ ...params.InputProps, type: "search" }}
              onChange={(e) =>
                setSearchData({ ...searchData, procedureType: e.target.value })
              }
            />
          )}
          onChange={(e: any, value: string) =>
            setSearchData({ ...searchData, procedureType: value })
          }
        />
        <Autocomplete
          freeSolo
          disableClearable
          options={filters.department.map((item) => item)}
          fullWidth
          value={searchData?.department ?? ""}
          renderInput={(params) => (
            <TextField
              placeholder={"Подразделение"}
              {...params}
              InputProps={{ ...params.InputProps, type: "search" }}
              onChange={(e) =>
                setSearchData({ ...searchData, department: e.target.value })
              }
            />
          )}
          onChange={(e: any, value: string) =>
            setSearchData({ ...searchData, department: value })
          }
        />
      </Stack>
      <Stack direction={"row"} sx={{ justifyContent: "right" }} gap={2}>
        <Button variant={"outlined"}>Отменить изменения</Button>
        <Button variant={"outlined"}>Сохранить</Button>
      </Stack>
    </Stack>
  );
};
