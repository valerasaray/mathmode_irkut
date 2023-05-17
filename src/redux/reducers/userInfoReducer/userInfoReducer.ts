import { IUserInfo } from "../../../models/authModels/IUserInfo";

enum actionTypes {
  SET_USER_INFO = "SET_USER_INFO",
  CLEAR_FIELDS_CREATOR = "CLEAR_FIELDS_CREATOR",
}

interface IActionProps {
  props: IUserInfo;
}

interface IAction {
  type: actionTypes;
  payload?: IActionProps;
}

interface IDefaultState {
  userInfo: IUserInfo;
}

const defaultState: IDefaultState = {
  userInfo: {},
};

const UserInfoReducer = (state = defaultState, action: IAction) => {
  switch (action.type) {
    case actionTypes.SET_USER_INFO:
      return {
        ...state,
        userInfo: { ...state.userInfo, ...action.payload },
      };
      break;
    default:
      return state;
  }
};

export default UserInfoReducer;

export const setUserInfo = (props: IUserInfo) => {
  return {
    type: actionTypes.SET_USER_INFO,
    payload: props,
  };
};
