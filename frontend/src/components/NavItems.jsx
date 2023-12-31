import { useContext, useState,useEffect  } from "react";
import { Link, NavLink } from "react-router-dom";
import logo from "../assets/images/logo/canje_xpress_logo.png";
import { AuthContext } from "../contexts/AuthProvider";
import { NavDropdown } from "react-bootstrap";

const NavItems = () => {
  const [menuToggle, setMenuToggle] = useState(false);
  const [socialToggle, setSocialToggle] = useState(false);
  const [headerFiexd, setHeaderFiexd] = useState(false);
  const [user, setUser] = useState({});

  // check if user is register
  const { user_data, logOut,authenticated } = useContext(AuthContext);

  useEffect(() => {
    // Llamar a user_data aquí para evitar el Warning de setState durante la renderización.
    user_data()
      .then(result => {
        setUser(result);
      })
      .catch(error => {
        console.error('Error capturing user data:', error);
      });
  }, [authenticated]); // Se ejecuta solo una vez al montar el component

  console.log(user)

  return (
    <header
      className={`header-section style-4 ${
        headerFiexd ? "header-fixed fadeInUp" : ""
      }`}
    >
      {/* ------ header top: first div ----- */}
      <div className={`header-top d-md-none ${socialToggle ? "open" : ""}`}>
        <div className="container">
          <div className="header-top-area">
            <Link to="/signup" className="lab-btn me-3">
              <span>Registrate</span>
            </Link>
            <Link to="/login">Iniciar Sesion</Link>
          </div>
        </div>
      </div>

      {/* header top ends*/}

      {/* ---header botton starts */}
      <div className="header-bottom">
        <div className="container">
          <div className="header-wrapper">
            {/* logo  */}
            <div className="logo-search-acte">
              <div className="logo">
                <Link to="/">
                  <img src={logo} alt="logo" />
                </Link>
              </div>
            </div>

            {/* menu area */}
            <div className="menu-area">
              <div className="menu">
                {/* <ul className={`lab-ul ${menuToggle ? "active" : ""}`}>
                  <li>
                    <Link to="/cart-page">Carrito</Link>
                  </li>
                </ul> */}
              </div>

              {/* users when user available */}
              {user ? (
                <>
                  <div>
                    {user?.photoURL ? (
                      <>
                        <img src={user?.photoURL} className="nav-profile" />
                      </>
                    ) : (
                      <img
                        src="/src/assets/images/author/01.jpg"
                        className="nav-profile"
                      />
                    )}
                  </div>
                  <NavDropdown id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1" onClick={logOut}>
                      Logout
                    </NavDropdown.Item>
                    <NavDropdown.Item href="/cart-page">
                      Shopping Cart
                    </NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">
                      Profile
                    </NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="/cart-page">Order</NavDropdown.Item>
                  </NavDropdown>
                </>
              ) : (
                <>
                  <Link
                    to="/sign-up"
                    className="lab-btn me-3 d-none d-md-block"
                  >
                    <span>Registrate</span>
                  </Link>
                  <Link to="/login" className="d-none d-md-block">
                    Iniciar Sesion
                  </Link>
                </>
              )}

              {/* menu toggle btn */}
              <div
                className={`header-bar d-lg-none ${menuToggle ? "active" : ""}`}
                onClick={() => setMenuToggle(!menuToggle)}
              >
                <span></span>
                <span></span>
                <span></span>
              </div>

              {/* social toggler */}
              <div
                className="ellepsis-bar d-md-none"
                onClick={() => setSocialToggle(!socialToggle)}
              >
                <i className="icofont-info-square"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* header botton ends */}
    </header>
  );
};

export default NavItems;
