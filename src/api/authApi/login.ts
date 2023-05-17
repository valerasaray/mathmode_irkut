import axios from "axios";
import { ILogin } from "../../models/authModels/ILogin";
import { IUserInfo } from "../../models/authModels/IUserInfo";
import { baseUrl, LOGIN } from "../../config/config";
import { Cookies } from "react-cookie";

const cookie = new Cookies();

export const login = async (
  data: ILogin,
  successCallback?: (prop: IUserInfo) => void,
  errorCallback?: () => void
) => {
  try {
    const response = await axios.post<IUserInfo>(baseUrl + "/user", {
      params: {
        login: data.login,
      },
      headers: {
        "Content-Type": "multipart/form-data",
      }
    });
    cookie.set(LOGIN, response?.data?.login);
    successCallback(response?.data);
  } catch (e) {
    console.error(e);
    errorCallback && errorCallback();
  }
};
