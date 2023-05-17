import { FC } from "react";
import { ITable } from "../../models/tableModels/ITable";
import { TableMatching } from "./Tables/TableMatching/TableMatching";

interface ITableFabricProps {
  isZoomable: number;
  isMatching: boolean;
  rowMatching: ITable;
}

export const TableFabric: FC<ITableFabricProps> = ({
  isZoomable,
  isMatching,
  rowMatching,
}) => {
  if (isMatching) {
    return <TableMatching rowMatching={rowMatching} isZoomable={isZoomable} />;
  }
  return <></>;
};
