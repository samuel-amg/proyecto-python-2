import PropTypes from 'prop-types';

import NewOrderSandwichListItem from './NewOrderSandwichListItem';

export default function NewOrderSandwichesList({ sandwiches, total }) {
  return (
    <>
      <span className="fs-4 fw-bolder">Resumen</span>
      {sandwiches.length
        ? (
          <div className="row">
            <div className="col-2">
              <span className="fw-bold">Nro.</span>
            </div>
            <div className="col-6">
              <span className="fw-bold">Nombre</span>
            </div>
            <div className="col-4 text-end">
              <span className="fw-bold">Precio</span>
            </div>
            {sandwiches.map((sandwich) => (
              <NewOrderSandwichListItem sandwich={sandwich} key={`sandwich-${sandwich.id}`} />
            ))}
          </div>
        )
        : (
          <span className="d-block text-black-50 text-center my-5">No hay items en la orden</span>
        )
      }
      {total !== 0 && (
        <div className="col-12 mt-5">
          <div className="d-flex justify-content-between">
            <span className="fw-bolder">Total:</span>
            <span className="fw-bold">{total}</span>
          </div>
        </div>
      )}
    </>
  );
}

NewOrderSandwichesList.propTypes = {
  sandwiches: PropTypes.array,
  total: PropTypes.number
};
