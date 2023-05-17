import { FC } from "react";
import { ITable } from "../../../../models/tableModels/ITable";
import { TableCell, TableRow } from "@mui/material";
import dayjs from "dayjs";

interface ITableReleasingProps {
  rowMatching: ITable;
}

export const TableReleasing: FC<ITableReleasingProps> = ({ rowMatching }) => {
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
              {phase?.subs[0].fit.FIO ?? ""}
            </TableCell>
            <TableCell>
              {dayjs(phase?.receipt).format("D MMMM YYYY").toString() ?? ""}
            </TableCell>
            <TableCell align="right">
              {dayjs(phase?.subs[0].start_verification).isValid()
                ? dayjs(phase?.subs[0].start_verification)
                    .format("D MMMM YYYY")
                    .toString()
                : ""}
            </TableCell>
            <TableCell align="right">
              {phase?.addenable ? "Да" : "Нет"}
            </TableCell>
            <TableCell align="right">
              {dayjs(phase?.subs[0].end_verification)
                .format("D MMMM YYYY")
                .toString() ?? ""}
            </TableCell>
            <TableCell align="right">
              {dayjs(phase?.subs[0].end_correction)
                .format("D MMMM YYYY")
                .toString() ?? ""}
            </TableCell>
          </>
        ))}
    </TableRow>
  );
};
