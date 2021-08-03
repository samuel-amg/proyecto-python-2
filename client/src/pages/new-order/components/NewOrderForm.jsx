import PropTypes from 'prop-types';

import useNewOrder from '../hooks/useNewOrder';

export default function NewOrderForm({
  addSandwich,
  addExtra,
  currentSandwichExtrasState,
  currentSandwichSizeState
}) {
  const {
    sandwichSizes,
    sandwichExtras
  } = useNewOrder();

  return (
    <div>
      <h4 className="fw-bolder mb-3">Información del Pedido</h4>
      <form>
        <div className="mb-3">
          <span className="d-block mb-3 fw-bold">Tamaño del Sandwich</span>
          <div className="row">
            {sandwichSizes.map((size) => (
              <div className="col-4 d-flex justify-content-center">
                <input
                  type="radio"
                  className="btn-check"
                  autoComplete="off"
                  id={`sandwich-size-${size.nombre}`}
                  name="size"
                  onClick={() => currentSandwichSizeState[1](size)}
                />
                <label
                  className={`btn btn-light bg-white text-center ${currentSandwichSizeState[0].nombre === size.nombre ? 'border border-5 border-info' : ''}`}
                  htmlFor={`sandwich-size-${size.nombre}`}
                >
                  <span>{size.nombre}</span>
                  <img
                    src="https://firebasestorage.googleapis.com/v0/b/sandwiches-los-guayaneses.appspot.com/o/icons8-sandwich.png?alt=media&token=178036b6-c3bb-4228-ba8a-b7c02726d1fd"
                    alt=""
                    className="img-fluid d-block mx-auto"
                  />
                  <span>{size.precio}</span>
                </label>
              </div>
            ))}
          </div>
        </div>
        <div className="mb-3">
          <span className="d-block mb-3 fw-bold">Extras (Opcional)</span>
          <div className="row g-3">
            {sandwichExtras.map((extra) => (
              <div className="col-3 text-center">
                <button
                  type="button"
                  className={`btn btn-light bg-white text-center ${currentSandwichExtrasState[0].some((extraItem) => extraItem.codigo === extra.codigo) ? 'shadow border border-5 border-info' : ''}`}
                  id={`sandwich-extra-${extra.nombre}`}
                  name={`sandwich-extra-${extra.nombre}`}
                  onClick={() => addExtra(extra)}
                >
                  <span className="fs-7">{extra.nombre}</span>
                  <img
                    src={extra.imagen}
                    alt=""
                    className="img-fluid d-block mx-auto"
                  />
                  <span>{extra.precio}</span>
                </button>
              </div>
            ))}
          </div>
        </div>
        <button type="submit" className="btn btn-secondary ms-auto" onClick={addSandwich}>
          Agregar Sandwich
        </button>
      </form>
    </div>
  );
}

NewOrderForm.propTypes = {
  addSandwich: PropTypes.func,
  addExtra: PropTypes.func,
  currentSandwichExtrasState: PropTypes.array,
  currentSandwichSizeState: PropTypes.array
};
