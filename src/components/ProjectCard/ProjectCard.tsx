import { FC } from "react";
import { ITable } from "../../models/tableModels/ITable";
import { Box, Divider, Paper, Stack, Typography } from "@mui/material";
import Blueprint from "../../assets/blueprint.png";
import { useNavigate } from "react-router-dom";

interface IProjectCardProps {
  rowMatching: ITable;
}

export const ProjectCard: FC<IProjectCardProps> = ({ rowMatching }) => {
  const navigate = useNavigate();
  return (
    <Paper
      onClick={() => navigate(`/table/${rowMatching?.id}`)}
      sx={{ ":hover": { cursor: "pointer" } }}
    >
      <Stack
        direction={"column"}
        sx={{
          alignContent: "center",
          textAlign: "center",
          justifyContent: "center",
        }}
        gap={1}
      >
        <Box
          sx={{
            width: "50px",
            height: "50px",
            backgroundImage: Blueprint,
            alignSelf: "center",
          }}
        >
          <img
            src={Blueprint}
            alt="blueprint"
            style={{ objectFit: "fill", width: "50px", height: "50px" }}
          />
        </Box>
        <Divider />
        <Typography variant={"caption"}>
          {rowMatching?.passport_ref ?? "Паспорт"}
        </Typography>
        <Typography variant={"caption"}>
          {rowMatching?.realiser?.login ?? "Автор"}
        </Typography>
      </Stack>
    </Paper>
  );
};
