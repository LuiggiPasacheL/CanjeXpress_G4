import "./list.scss"
import Sidebar from "../../../components/Backoffice/sidebar/Sidebar"
import Navbar from "../../../components/Backoffice/navbar/Navbar"
import ProductDatatable from "../../../components/Backoffice/datatable/ProductDatatable"

const List = () => {
  return (
    <div className="list">
      <Sidebar/>
      <div className="listContainer">
        <Navbar/>
        <ProductDatatable/>
      </div>
    </div>
  )
}

export default List