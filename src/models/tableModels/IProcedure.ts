export interface IProcedure {
  id?: string;
  passport_ref?: string;
  realiser?: {
    id?: string;
    login?: string;
  };
  realiserGroup?: {
    id?: string;
    title?: string;
  };
  processType?: {
    id?: string;
    value?: string;
  };
}
