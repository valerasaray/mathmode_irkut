import { useState } from "react";
import { Link } from "react-router-dom";

export const NavTool = () => {
  const [activeState, setActiveState] = useState<boolean>();
  return (
    <div
      className="nav-tool"
      style={{
        width: "fit-content",
        position: "fixed",
        right: 0,
        bottom: 0,
        paddingRight: "10px",
        paddingBottom: "20px",
        overflow: "hidden",
      }}
    >
      <div
        className="nav-tool__btn"
        onClick={() => setActiveState((activeState) => !activeState)}
        style={{ cursor: "pointer", fontSize: "40px", textAlign: "end" }}
      >
        {activeState ? ">" : "<"}
      </div>
      <div
        className="nav-tool__panel"
        style={{
          width: "fit-content",
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-end",
          justifyContent: "center",
          transform: `translateX(${activeState ? "0" : "150%"})`,
          transition: "all 0.2s",
        }}
      >
        <Link to={"/"}>TablePage</Link>
        <Link to={"/auth"}>Authorization</Link>
      </div>
    </div>
  );
};
