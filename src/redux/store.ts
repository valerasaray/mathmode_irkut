import { combineReducers, configureStore } from "@reduxjs/toolkit";
import ModalReducer from "./reducers/modalReducer/modalReducer";
import FilterReducer from "./reducers/filterReducer/filterReducer";
import UserInfoReducer from "./reducers/userInfoReducer/userInfoReducer";

export type RootState = ReturnType<typeof store.getState>;

const rootReducer = combineReducers({
  modal: ModalReducer,
  filter: FilterReducer,
  userInfo: UserInfoReducer,
});

const store = configureStore({
  reducer: rootReducer,
});

export default store;
