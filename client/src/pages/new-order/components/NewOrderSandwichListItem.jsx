import PropTypes from 'prop-types';

export default function NewOrderSandwichListItem({
  sandwich: {
    index,
    size: {
      nombre,
      precio
    },
    precio: price,
    extras
  }
}) {
  return (
    <>
      <div className="col-2">
        <div className="rounded-circle bg-gray-100 p-2 d-flex align-items-center justify-content-center">
          <small>{index}</small>
        </div>
      </div>
      <div className="col-6 d-flex align-items-center">
        <span>{nombre}</span>
      </div>
      <div className="col-4 d-flex align-items-center justify-content-end">
        <span className="text-black-50 fw-bold">{precio}</span>
      </div>
      {extras.map((extra) => (
        <>
          <div className="col-2" />
          <div className="col-6">
            <small className="text-black-50">{extra.nombre}</small>
          </div>
          <div className="col-4 text-end">
            <small className="text-black-50">{extra.precio}</small>
          </div>
        </>
      ))}
      <div className="col-2" />
      <div className="col-10 text-end border-top mt-2 pt-2">
        <span className="text-black-50 fw-bold">{price}</span>
      </div>
    </>
  );
}

NewOrderSandwichListItem.propTypes = {
  sandwich: PropTypes.shape({
    index: PropTypes.string.isRequired,
    precio: PropTypes.number.isRequired,
    size: PropTypes.shape({
      precio: PropTypes.number,
      nombre: PropTypes.string
    }),
    extras: PropTypes.array.isRequired
  })
};
