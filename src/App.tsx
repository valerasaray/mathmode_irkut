import dayjs from "dayjs";
import { Navigate, Route, Routes } from "react-router-dom";
import { AuthenticatePage } from "./pages/AuthenticatePage/AuthenticatePage";
import { TablePage } from "./pages/TablePage/TablePage";
import { NavTool } from "./components/NavTool/NavTool";
import { Header } from "./components/Header/Header";
import { GrapthPage } from "./pages/GrapthPage/GrapthPage";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { login } from "./api/authApi/login";
import { Cookies } from "react-cookie";
import { LOGIN } from "./config/config";
import { setUserInfo } from "./redux/reducers/userInfoReducer/userInfoReducer";

const cookie = new Cookies();

function App() {
  dayjs.locale("ru");
  const dispatch = useDispatch();
  useEffect(() => {
    login(cookie.get(LOGIN), (value) => dispatch(setUserInfo(value)));
  }, []);
  return (
    <>
      <Header />
      <Routes>
        <Route index element={<Navigate to={"/table"} />} />
        <Route path={"/auth"} element={<AuthenticatePage />} />
        <Route path={"/table"} element={<TablePage />} />
        <Route path={"/table/:id"} element={<GrapthPage />} />
      </Routes>
      <NavTool />
    </>
  );
}

export default App;
