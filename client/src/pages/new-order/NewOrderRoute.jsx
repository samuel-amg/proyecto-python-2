import NewOrderClientData from './components/NewOrderClientData';
import NewOrderSandwichesList from './components/NewOrderSandwichesList';
import NewOrderForm from './components/NewOrderForm';

export default function NewOrderRoute() {
  return (
    <div className="py-5">
      <div className="row">
        <div className="col-8">
          <div className=" d-flex flex-column justify-content-center rounded-3 p-4 shadow-sm bg-white w-100">
            <NewOrderClientData />
            <NewOrderForm />
          </div>
        </div>
        <div className="col-4">
          <NewOrderSandwichesList />
        </div>
      </div>
    </div>
  );
}
