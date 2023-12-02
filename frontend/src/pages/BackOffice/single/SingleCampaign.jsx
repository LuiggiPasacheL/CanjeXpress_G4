import "./single.scss";
import Sidebar from "../../../components/Backoffice/sidebar/Sidebar";
import Navbar from "../../../components/Backoffice/navbar/Navbar";

const SingleCampaign = ({currentCampaign}) => {

  return (
    <div className="single">
      <Sidebar />
      <div className="singleContainer">
        <Navbar />
        <div className="top">
          <div className="left">
            <div className="editButton">Edit</div>
            <h1 className="title">Información de la campaña</h1>
            <div className="item">
              <div className="details">
                <h1 className="itemTitle">{currentCampaign.name}</h1>
                <div className="detailItem">
                  <span className="itemKey">Fecha de Inicio: </span>
                  <span className="itemValue">{currentCampaign.start_date}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Fecha de Cierre: </span>
                  <span className="itemValue">{currentCampaign.end_date}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Descuento</span>
                  <span className="itemValue">{currentCampaign.discount}</span>
                </div>
                <div className="detailItem">
                  <span className="itemKey">Marcas</span>
                  <span className="itemValue">{currentCampaign.brands}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SingleCampaign;
