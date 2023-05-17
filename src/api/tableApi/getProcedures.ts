import { baseUrl } from "../../config/config";
import { ITable } from "../../models/tableModels/ITable";
import axios from "axios";
const defaultTable: ITable[] = [
  {
    realiser: {
      id: "",
      login: "Петров В.В.",
    },
    passport_ref: "T7-1410-22 NC",
    realiserGroup: {
      id: "",
      title: "Отделение планера",
    },
    processType: {
      id: "",
      value: "ИИ",
    },
    nodes: [
      {
        id: "1",
        receipt: "234125",
        title: "Этап проверки 1",
        addenable: false,
        subs: [
          {
            end_correction: "1",
            end_verification: "1",
            fit: {
              id: "2",
              FIO: "Петров В.В.",
            },
            id: "15",
            start_verification: "2",
            title: "41234",
          },
        ],
      },
      {
        id: "2",
        receipt: "242",
      },
    ],
  },
  {
    realiser: {
      id: "",
      login: "Петров В.В.",
    },
    passport_ref: "T7-1410-22 NC",
    realiserGroup: {
      id: "",
      title: "Отделение планера",
    },
    processType: {
      id: "",
      value: "ИИ",
    },
    nodes: [
      {
        id: "1",
        receipt: "234125",
        title: "Этап проверки 1",
        addenable: false,
        subs: [
          {
            end_correction: "1",
            end_verification: "1",
            fit: {
              id: "2",
              FIO: "Петров В.В.",
            },
            id: "15",
            start_verification: "2",
            title: "41234",
          },
        ],
      },
      {
        id: "2",
        receipt: "242",
      },
    ],
  },
  {
    realiser: {
      id: "",
      login: "Петров В.И.",
    },
    passport_ref: "T7-1410-22 NC",
    realiserGroup: {
      id: "",
      title: "Отделение планера",
    },
    processType: {
      id: "",
      value: "ИИ",
    },
    nodes: [
      {
        id: "1",
        receipt: "234125",
        title: "Этап проверки 1",
        addenable: false,
        subs: [
          {
            end_correction: "1",
            end_verification: "1",
            fit: {
              id: "2",
              FIO: "Петров В.В.",
            },
            id: "15",
            start_verification: "2",
            title: "41234",
          },
        ],
      },
      {
        id: "2",
        receipt: "242",
      },
    ],
  },
];

export const getProcedures = async (
  params: string,
  successCallback?: (props: ITable[]) => void,
  errorCallback?: () => void,
  isDefault?: boolean
) => {
  try {
    if (isDefault) {
      successCallback(defaultTable);
    } else {
      try {
        const response = await axios.post<ITable[]>(
          baseUrl + "/processes/realizer",
          {
            params: {
              login: params,
            },
          }
        );

        successCallback(response?.data);
      } catch (e) {
        console.error(e);
        errorCallback && errorCallback();
      }
    }
  } catch (e) {
    console.error(e);
    errorCallback && errorCallback();
  }
};
