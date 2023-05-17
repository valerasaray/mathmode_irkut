import { Button, Paper, Stack, TextField } from "@mui/material";
import Factory from "../../assets/irkut-factory-2.jpg";
import { ILogin } from "../../models/authModels/ILogin";
import { useState } from "react";
import { login } from "../../api/authApi/login";
import { setUserInfo } from "../../redux/reducers/userInfoReducer/userInfoReducer";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";

const loginDefault: ILogin = {
  login: "",
  password: "",
};

export const AuthenticatePage = () => {
  const [loginData, setLoginData] = useState<ILogin>(loginDefault);

  const dispatch = useDispatch();

  const navigate = useNavigate();

  const handlerLogin = () => {
    login(
      loginData,
      (value) => {
        dispatch(setUserInfo(value));
        navigate("/table");
      },
      undefined
    );
  };
  return (
    <Stack
      direction={"row"}
      sx={{
        backgroundImage: `url(${Factory})`,
        backgroundSize: "cover",
        width: "100%",
        height: "100vh",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Paper sx={{ height: "50%" }} elevation={5}>
        <img
          src={"https://www.irkut.com/img/logo_ru.svg"}
          alt={"Иркутск"}
          style={{ width: "370px" }}
        />
        <Stack direction={"column"} gap={2} mt={3} padding={4}>
          <TextField
            placeholder={"Логин"}
            value={loginData.login ?? ""}
            onChange={(e) =>
              setLoginData({ ...loginData, login: e.target.value })
            }
            required
          />
          <TextField
            placeholder={"Пароль"}
            value={loginData.password ?? ""}
            onChange={(e) =>
              setLoginData({ ...loginData, password: e.target.value })
            }
            required
          />
          <Button
            variant={"high"}
            sx={{ width: "100%" }}
            onClick={handlerLogin}
          >
            Авторизоваться
          </Button>
        </Stack>
      </Paper>
    </Stack>
  );
};
