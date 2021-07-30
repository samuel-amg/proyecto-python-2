import { useHistory } from 'react-router-dom';

import Logo from '../../components/Logo';

export default function HomeRoute() {
  const router = useHistory();
  return (
    <div className="d-flex flex-column align-items-center text-center py-5">
      <h1 className="fw-bolder">Sandwiches Los Guayaneses</h1>
      <Logo width="600px" height="300px" />
      <div className="d-flex justify-content-evenly w-100">
        <button
          type="button"
          className="btn btn-light text-white bg-gunmetal"
          onClick={() => router.push('/new-order')}
        >
          Nuevo Pedido
        </button>
        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => router.push('/admin')}
        >
          Administración
        </button>
      </div>
    </div>
  );
}
