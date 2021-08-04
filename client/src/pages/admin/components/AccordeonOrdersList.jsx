import PropTypes from 'prop-types';

import NewOrderSandwichesList from '../../new-order/components/NewOrderSandwichesList';

export default function AccordionOrdersList({ orders }) {
  return (
    <div className="accordion accordion-flush" id="ordersAccordeon">
      {orders.map((order, i) => (
        <div className="accordion-item">
          <h2 className="accordion-header" id={`flush-heading-${i}`}>
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target={`#flush-collapse-${i}`}
              aria-expanded="false"
              aria-controls={`flush-collapse-${i}`}
            >
              {`Orden #${order.id}`}
            </button>
          </h2>
          <div
            id={`flush-collapse-${i}`}
            className="accordion-collapse collapse"
            aria-labelledby={`flush-heading-${i}`}
            data-bs-parent="#ordersAccordeon"
          >
            <div className="accordion-body">
              <h5 className="mb-3 fw-bolder">
                {'Cliente: '}
                {order.cliente}
              </h5>
              <NewOrderSandwichesList sandwiches={order.sandwiches} total={order.total} />
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

AccordionOrdersList.propTypes = {
  orders: PropTypes.array.isRequired
};
