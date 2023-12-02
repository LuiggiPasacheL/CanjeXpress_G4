import "./navbar.scss";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import Avatar from '@mui/material/Avatar';
import { deepOrange } from '@mui/material/colors';
import NotificationsNoneOutlinedIcon from "@mui/icons-material/NotificationsNoneOutlined";
import { useContext } from "react";

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="wrapper">
        <div className="search">
          <input type="text" placeholder="Buscar..." />
          <SearchOutlinedIcon />
        </div>
        <div className="items">
          <div className="item">
            <NotificationsNoneOutlinedIcon className="icon" />
            <div className="counter">1</div>
          </div> 
          <div className="item">
            <Avatar sx={{ bgcolor: deepOrange[500] }}>AD</Avatar>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
