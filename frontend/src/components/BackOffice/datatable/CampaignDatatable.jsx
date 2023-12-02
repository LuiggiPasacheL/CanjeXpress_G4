import "./datatable.scss";
import { DataGrid } from "@mui/x-data-grid";
import { campaignColumns, campaignRows } from "../../../utilis/datatablesource";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../../../contexts/AuthProvider';

const CampaignDatatable = () => {
  const [data, setData] = useState(campaignRows);

  const { authenticated, user_data } = useContext(AuthContext);
  const [campaigns, setCampaigns] = useState([]);

  useEffect(() => {
    const fetchCampaigns = async () => {
      try {
        if (authenticated) {
          const userData = await user_data();
          
          const response = await fetch('http://34.125.103.185/api/backoffice/backoffice/campaigns', {
            method: 'GET',
            mode: 'no-cors',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
            },
          });

          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const data = await response.json();
          setCampaigns(data);
        }
      } catch (error) {
        console.error('Error fetching campaigns:', error);
        console.log('Response status:', response.status);
        console.log('Response text:', await response.text());
      }
    };

    fetchCampaigns();
    console.log(campaigns);
  }, [authenticated, user_data]);

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
            <Link to="/backoffice/campaigns/campaign.id" style={{ textDecoration: "none" }}>
              <div className="viewButton">Ver</div>
            </Link>
            <div
              className="deleteButton"
              onClick={() => handleDelete(params.row.id)}
            >
              Eliminar
            </div>
          </div>
        );
      },
    },
  ];

  return (

    

    <div className="datatable">
      <div className="datatableTitle">
        Campañas
        <Link to="/backoffice/campaigns/newCampaign" className="link">
          Nueva campaña
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

export default CampaignDatatable;
