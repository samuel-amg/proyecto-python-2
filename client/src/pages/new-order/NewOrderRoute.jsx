import NewOrderClientData from './components/NewOrderClientData';
import NewOrderSandwichesList from './components/NewOrderSandwichesList';
import NewOrderForm from './components/NewOrderForm';
import useNewOrder from './hooks/useNewOrder';

export default function NewOrderRoute() {
  const {
    sandwiches,
    addSandwich,
    addSandwichExtra,
    currentSandwichExtrasState,
    currentSandwichSizeState,
    orderTotal,
    clientNameState,
    blockClientNameState,
    createOrder
  } = useNewOrder();

  console.log(sandwiches);
  return (
    <div className="py-5">
      <div className="row">
        <div className="col-8">
          <div className=" d-flex flex-column justify-content-center rounded-3 p-4 shadow-sm bg-white w-100">
            <NewOrderClientData
              blockClientNameState={blockClientNameState}
              clientNameState={clientNameState}
            />
            {(blockClientNameState[0] || sandwiches.length) && (
              <NewOrderForm
                addSandwich={addSandwich}
                addExtra={addSandwichExtra}
                currentSandwichExtrasState={currentSandwichExtrasState}
                currentSandwichSizeState={currentSandwichSizeState}
              />
            )}
          </div>
        </div>
        <div className="col-4">
          <div className="rounded-3 p-4 shadow-sm bg-white">
            <NewOrderSandwichesList sandwiches={sandwiches} total={orderTotal} />
            <button type="button" className="btn bg-burnt-sienna w-100 text-white fw-bolder" onClick={createOrder}>Crear Pedido</button>
          </div>
        </div>
      </div>
    </div>
  );
}
