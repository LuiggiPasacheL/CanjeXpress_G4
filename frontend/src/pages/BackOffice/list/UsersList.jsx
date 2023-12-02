import "./list.scss"
import Sidebar from "../../../components/Backoffice/sidebar/Sidebar"
import Navbar from "../../../components/Backoffice/navbar/Navbar"
import UserDatatable from "../../../components/BackOffice/datatable/UserDatatable"

const List = () => {
  return (
    <div className="list">
      <Sidebar/>
      <div className="listContainer">
        <Navbar/>
        <UserDatatable/>
      </div>
    </div>
  )
}

export default List