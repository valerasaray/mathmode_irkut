import { FC } from "react";
import { ITable } from "../../../../models/tableModels/ITable";
import { TableCell } from "@mui/material";

interface ITableColumnsProps {
  rowMatching?: ITable;
  isPhase: boolean;
}

export const TableColumns: FC<ITableColumnsProps> = ({
  rowMatching,
  isPhase = true,
}) => {
  if (isPhase) {
    return (
      <>
        {rowMatching?.nodes &&
          rowMatching?.nodes.map((phase, index) => (
            <TableCell key={index} colSpan={6}>
              {phase?.title}
            </TableCell>
          ))}
      </>
    );
  }
  return (
    <>
      {rowMatching?.nodes &&
        rowMatching?.nodes.map(() => (
          <>
            <TableCell>Фамилия согласующего</TableCell>
            <TableCell>Дата поступления документа</TableCell>
            <TableCell align="right">Дата проверки документа</TableCell>
            <TableCell align="right">Наличие замечаний</TableCell>
            <TableCell align="right">Дата согласования</TableCell>
            <TableCell align="right">Дата подписания</TableCell>
          </>
        ))}
    </>
  );
};
