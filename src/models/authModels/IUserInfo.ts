export interface IUserInfo {
  id?: string;
  login?: string;
  FIO?: string;
  rights?: IRight[];
}

interface IRight {
  id: string;
  value: string;
}
