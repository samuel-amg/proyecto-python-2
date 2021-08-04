import useAdmin from './hooks/useAdmin';
import AccordionOrdersList from './components/AccordeonOrdersList';

export default function AdminRoute() {
  const {
    filterParam,
    onChangeFilter,
    inputValue,
    onChange,
    sizes,
    extras,
    getReport,
    orders
  } = useAdmin();

  console.log(filterParam);

  return (
    <div className="py-5">
      <h1 className="text-center fw-bolder">Reportes de Administración</h1>
      <div className="mt-3">
        <span className="d-block fw-bold">Filtros</span>
        <div className="row">
          <div className="col-3">
            <select className="form-select" aria-label="FilterSelect" onChange={onChangeFilter}>
              <option selected value="">Todos</option>
              <option value="by_client">Por Cliente</option>
              <option value="by_size">Por Tamaño de Sandwich</option>
              <option value="by_date">Por Fecha</option>
              <option value="by_ingredient">Por Extra</option>
            </select>
          </div>
          <div className={`col-3 ${filterParam ? 'd-block' : 'd-none'}`}>
            {filterParam === 'by_client' && (
              <input
                type="text"
                className="form-control"
                id="clientName"
                placeholder="Nombre del Cliente"
                value={inputValue}
                onChange={onChange}
              />
            )}
            {filterParam === 'by_size' && (
              <select className="form-select" aria-label="FilterSelect" onChange={onChange}>
                <option selected value="">Seleccione un tamaño</option>
                {sizes.map((size) => (
                  <option key={`size-${size.id}`} value={size.id}>{size.nombre}</option>
                ))}
              </select>
            )}
            {filterParam === 'by_date' && (
              <input
                type="text"
                className="form-control"
                id="date"
                placeholder="2021-08-11"
                value={inputValue}
                onChange={onChange}
              />
            )}
            {filterParam === 'by_ingredient' && (
              <select className="form-select" aria-label="FilterSelect" onChange={onChange}>
                <option selected value="">Seleccione un Extra</option>
                {extras.map((extra) => (
                  <option key={`extra-${extra.id}`} value={extra.id}>{extra.nombre}</option>
                ))}
              </select>
            )}
          </div>
          <div className="col-2">
            <button
              className="btn btn-primary fw-bolder text-white btn-block w-100"
              type="button"
              onClick={getReport}
            >
              Filtrar
            </button>
          </div>
        </div>
        <div className="mt-5">
          <h3 className="text-center mb-5 fw-bold">Órdenes</h3>
          {orders.length
            ? (
              <div className="container">
                <AccordionOrdersList orders={orders} />
              </div>
            )
            : (
              <h5 className="text-center text-black-50">No hay ordenes que mostrar</h5>
            )
          }
        </div>
      </div>
    </div>
  );
}
