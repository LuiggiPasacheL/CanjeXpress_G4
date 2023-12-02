import "./datatable.scss";
import { DataGrid } from "@mui/x-data-grid";
import { campaignColumns, userRows } from "../../../utilis/datatablesource";
import { Link } from "react-router-dom";
import { useState } from "react";

const ProductDatatable = () => {
  const [data, setData] = useState(userRows);

  const handleDelete = (id) => {
    setData(data.filter((item) => item.id !== id));
  };

  const actionColumn = [
    {
      field: "action",
      headerName: "Action",
      width: 200,
      renderCell: (params) => {
        return (
          <div className="cellAction">
            <Link to="/backoffice/products/{product.id}" style={{ textDecoration: "none" }}>
              <div className="viewButton">View</div>
            </Link>
            <div
              className="deleteButton"
              onClick={() => handleDelete(params.row.id)}
            >
              Delete
            </div>
          </div>
        );
      },
    },
  ];

  return (
    <div className="datatable">
      <div className="datatableTitle">
        Usuarios
        <Link to="/backoffice/products/newProduct" className="link">
          Crear nuevo 
        </Link>
      </div>
      <DataGrid
        className="datagrid"
        rows={data}
        columns={campaignColumns.concat(actionColumn)}
        pageSize={10}
        rowsPerPageOptions={[10]}
        checkboxSelection
      />
    </div>
  );
};

export default ProductDatatable;
