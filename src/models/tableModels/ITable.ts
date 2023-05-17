import { IProcedure } from "./IProcedure";

export interface ITable extends IProcedure {
  nodes: IPhase[];
}

interface IPhase {
  id?: string;
  title?: string;
  addenable?: boolean;
  subs?: {
    id?: string;
    title?: string;
    start_verification?: string;
    end_verification?: string;
    end_correction?: string;
    fit?: {
      id?: string;
      FIO?: string;
    };
  }[];
  receipt?: string;
  next?: {
    id?: string;
  };
}
