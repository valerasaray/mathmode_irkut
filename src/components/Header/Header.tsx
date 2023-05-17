import {
  Paper,
  Button,
  Menu,
  MenuItem,
  Stack,
  Typography,
} from "@mui/material";
import { useState } from "react";
import { useLocation } from "react-router-dom";

export const Header = () => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);

  const location = useLocation();

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  if (location.pathname === "/auth") {
    return <></>;
  }

  return (
    <Paper variant={"header"} sx={{ width: "100%" }}>
      <Stack
        className="header__wrapper"
        direction={"row"}
        sx={{
          alignItems: "center",
          width: "100%",
          height: "100%",
          justifyContent: "space-between",
        }}
      >
        <img
          src={"https://www.irkut.com/img/logo_ru.svg"}
          alt={"Иркутск"}
          style={{ width: "100px" }}
        />
        <Stack direction={"row"}>
          <Typography variant={"caption"} sx={{ marginTop: "6px" }}>
            Фамилия Имя
          </Typography>
          <Button
            id="basic-button"
            variant={"textButton"}
            aria-controls={open ? "basic-menu" : undefined}
            aria-haspopup="true"
            aria-expanded={open ? "true" : undefined}
            onClick={handleClick}
          >
            Меню
          </Button>
          <Menu
            id="basic-menu"
            anchorEl={anchorEl}
            open={open}
            onClose={handleClose}
            MenuListProps={{
              "aria-labelledby": "basic-button",
            }}
          >
            <MenuItem onClick={handleClose}>Выгрузить таблицу</MenuItem>
            <MenuItem onClick={handleClose}>Сообщить в подержку</MenuItem>
            <MenuItem onClick={handleClose}>Выход</MenuItem>
          </Menu>
        </Stack>
      </Stack>
    </Paper>
  );
};
