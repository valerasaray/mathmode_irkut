import { Dialog, DialogContent, Typography } from "@mui/material";
import { useDispatch } from "react-redux";
import {
  isModalActive,
  setModalInactive,
} from "../../../redux/reducers/modalReducer/modalReducer";
import { useSelector } from "react-redux";
import { RootState } from "../../../redux/store";

export const CreateProcessModal = () => {
  const activeModals = useSelector(
    (state: RootState) => state.modal.activeModals
  );
  const dispatch = useDispatch();
  return (
    <Dialog
      className="create_process"
      open={isModalActive("createProcessModal", activeModals)}
      onClose={() => dispatch(setModalInactive("createProcessModal"))}
      fullWidth
      maxWidth={"sm"}
    >
      <DialogContent>
        <Typography variant={"h5"}>Создание процесса</Typography>
      </DialogContent>
    </Dialog>
  );
};
