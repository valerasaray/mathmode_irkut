import { createTheme } from "@mui/material";
import {
  blackColor,
  darkBlueColor,
  grayColor,
  lightBlueColor,
  lightGrayColor,
  whiteColor,
} from "../color/color";

declare module "@mui/material/Button" {
  interface ButtonPropsVariantOverrides {
    high: true;
    whiteColor: true;
    textButton: true;
    fileInput: true;
    weakTextButton: true;
    arrowButton: true;
  }
}

declare module "@mui/material/InputBase" {
  interface InputBasePropsColorOverrides {
    whiteColor: true;
    lightBlueColor: true;
  }
}

declare module "@mui/material/Paper" {
  interface PaperPropsVariantOverrides {
    helpButton: true;
    bigPadding: true;
    header: true;
    whiteBlue: true;
  }
}

export const theme = createTheme({
  typography: {
    fontFamily: "Roboto",
    h3: {
      fontFamily: "Jost",
      fontWeight: "800",
      fontSize: "50px",
      lineHeight: "50px",
    },
    h4: {
      fontFamily: "Jost",
      fontWeight: "800",
      fontSize: "34px",
      lineHeight: "40px",
      letterSpacing: "0.25px",
    },
    h5: {
      fontFamily: "Jost",
      fontWeight: "800",
      fontSize: "24px",
      lineHeight: "32px",
    },
    h6: {
      fontFamily: "Jost",
      fontWeight: "800",
      fontSize: "18px",
      lineHeight: "18px",
    },
    button: {
      fontFamily: "Jost",
      fontWeight: "700",
      fontSize: "20px",
      lineHeight: "20px",
    },
    caption: {
      fontFamily: "Roboto",
      fontWeight: "400",
      fontSize: "16px",
      lineHeight: "20px",
    },
    body2: {
      fontFamily: "Roboto",
      fontWeight: "400",
      fontSize: "14px",
      lineHeight: "20px",
    },
  },
  components: {
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          backgroundColor: lightBlueColor,
          borderRadius: "30px",
          height: "50px",
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          width: "100%",
          input: {
            width: "100%",
            height: "50px",
            padding: "6px",
            borderRadius: "30px",
            border: "none",
            color: blackColor,
            fontSize: "16px",
            lineHeight: "20px",
            fontFamily: "Roboto",
            fontWeight: "400",
            boxSizing: "border-box",
            "&::placeholder": {
              color: grayColor,
              opacity: "1",
              fontSize: "16px",
              lineHeight: "20px",
              fontFamily: "Roboto",
              fontWeight: "400",
            },

            "&::-webkit-outer-spin-button": {
              "-webkit-appearance": "none",
            },
            "&::-webkit-inner-spin-button": {
              "-webkit-appearance": "none",
            },
          },
          "& .MuiOutlinedInput-root": {
            "&:hover fieldset": {
              borderColor: lightBlueColor,
            },
          },
          "& .MuiInputBase-colorPrimary": {
            "&:hover fieldset": {
              borderColor: lightBlueColor,
            },
            input: {
              "&:-webkit-autofill": {
                WebkitBoxShadow: `0 0 0 1000px ${lightBlueColor} inset`,
                borderRadius: "30px",
              },
            },
          },
          "& .MuiInputBase-colorSecondary": {
            "&:hover fieldset": {
              borderColor: "#FFF",
            },
            input: {
              "&:-webkit-autofill": {
                WebkitBoxShadow: `0 0 0 1000px #FFF inset`,
                borderRadius: "30px",
              },
            },
          },
          "& .MuiInputBase-colorSecondary.Mui-focused, .MuiInputBase-colorSecondary.Mui-disabled":
            {
              fieldset: {
                borderColor: "#FFF",
              },
            },
          "& .MuiInputBase-colorSecondary.MuiOutlinedInput-root": {
            backgroundColor: "#FFF",
          },
          "& .Mui-error": {
            "&:hover fieldset": {
              borderColor: "#d32f2f",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#d32f2f",
            },
          },
          "& .Mui-disabled": {
            "& .MuiOutlinedInput-notchedOutline": {
              border: "none",
            },
          },
        },
      },
    },
    MuiInputBase: {
      styleOverrides: {
        root: {
          padding: "0 15px 0 12px !important ",
        },
      },
      variants: [
        {
          props: { color: "primary" },
          style: {
            input: {
              backgroundColor: lightBlueColor,
              borderRadius: "30px",
            },
            fieldset: {
              borderColor: lightBlueColor,
            },
          },
        },
        {
          props: { color: "secondary" },
          style: {
            input: {
              backgroundColor: "#FFF",
              borderRadius: "30px",
            },
            fieldset: {
              borderColor: "#FFF",
            },
          },
        },
      ],
    },
    MuiAccordion: {
      styleOverrides: {
        root: {
          backgroundColor: lightGrayColor,
          borderRadius: 20,
          "&.MuiPaper-root": {
            borderRadius: 20,
            padding: 0,
          },
          "&:before": {
            backgroundColor: "rgba(0,0,0,0)",
          },
        },
      },
    },
    MuiAccordionSummary: {
      styleOverrides: {
        root: {
          backgroundColor: whiteColor,
          borderRadius: 20,
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 20,
          padding: 30,
          "&.MuiPickersPopper-paper": {
            padding: 5,
          },
        },
      },
      variants: [
        {
          props: { variant: "header" },
          style: {
            padding: 0,
            paddingLeft: "15px",
            paddingRight: "15px",
            backgroundColor: lightBlueColor,
            height: 55,
            borderRadius: 0,
          },
        },
      ],
    },
    MuiButton: {
      styleOverrides: {
        root: {
          minWidth: "fit-content",
          width: "fit-content",
          padding: "0 16px",
          backgroundColor: darkBlueColor,
          height: "30px",
          borderRadius: "30px",
          fontFamily: "Jost",
          fontWeight: "700",
          fontSize: "20px",
          lineHeight: "20px",
          color: whiteColor,
          textTransform: "none",
          "&:hover": { backgroundColor: darkBlueColor },
          "&.Mui-disabled": {
            backgroundColor: "#97d5e4",
            color: whiteColor,
          },
        },
      },
      variants: [
        {
          props: { variant: "high" },
          style: {
            height: "50px",
          },
        },
        {
          props: { variant: "textButton" },
          style: {
            backgroundColor: "transparent",
            "&:hover": { backgroundColor: "transparent" },
            color: darkBlueColor,
          },
        },
        {
          props: { variant: "weakTextButton" },
          style: {
            backgroundColor: "transparent",
            "&:hover": { backgroundColor: "transparent" },
            color: darkBlueColor,
            fontFamily: "Montserrat",
            fontSize: "16px",
            fontWeight: 400,
            padding: 5,
          },
        },
        {
          props: { variant: "fileInput" },
          style: {
            backgroundColor: lightBlueColor,
            width: "100%",
            height: "50px",
            display: "flex",
            justifyContent: "space-between",
            "&:hover": { backgroundColor: lightBlueColor },
            color: darkBlueColor,
          },
        },
        {
          props: { variant: "arrowButton" },
          style: {
            minWidth: "34px",
            width: "fit-content",
            backgroundColor: whiteColor,
            color: darkBlueColor,
            borderRadius: "100%",
            height: "34px",
            padding: "0",
          },
        },
      ],
    },
  },
});
