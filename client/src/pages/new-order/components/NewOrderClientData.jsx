import { IoPencil } from 'react-icons/io5';

import useNewOrder from '../hooks/useNewOrder';

export default function NewOrderClientData() {
  const { clientNameState, blockClientNameState } = useNewOrder();

  return (
    <div className="mb-5">
      <h4 className="fw-bolder text-body">Nombre del Cliente</h4>
      <input
        disabled={blockClientNameState[0]}
        type="text"
        className="form-control my-3"
        value={clientNameState[0]}
        onChange={(e) => clientNameState[1](e.target.value)}
        placeholder="Pedro Pérez"
      />
      <button
        className="btn btn-primary fw-bolder text-white btn-block"
        type="button"
        onClick={() => {
          if (clientNameState[0] && !blockClientNameState[0]) {
            blockClientNameState[1](true);
          }
          if (blockClientNameState[0]) {
            blockClientNameState[1](false);
          }
        }}
      >
        {blockClientNameState[0] ? 'Editar' : 'Continuar'}
        {blockClientNameState[0] && <IoPencil className="ms-2" />}
      </button>
    </div>
  );
}
