import "./list.scss"
import Sidebar from "../../../components/Backoffice/sidebar/Sidebar"
import Navbar from "../../../components/Backoffice/navbar/Navbar"
import CampaignDatatable from "../../../components/Backoffice/datatable/CampaignDatatable"

const CampaignsList = () => {
  return (
    <div className="list">
      <Sidebar/>
      <div className="listContainer">
        <Navbar/>
        <CampaignDatatable />
      </div>
    </div>
  )
}

export default CampaignsList