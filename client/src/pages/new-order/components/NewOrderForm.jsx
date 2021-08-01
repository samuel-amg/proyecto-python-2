// import { useForm} from 'react-hook-form';
import useNewOrder from '../hooks/useNewOrder';
import SandwichSvg from '../../../assets/food-icons/icons8-sandwich.png';

export default function NewOrderForm() {
  // const { /* handleSubmit, register, */ } = useForm();
  const {
    // sandwichExtras,
    sandwichSizes,
    currentSandwichSizeState
    /* currentSandwichExtrasState,
    addSandwich */
  } = useNewOrder();
  return (
    <div className="mb-5">
      <h4 className="fw-bolder mb-3">Información del Pedido</h4>
      <form>
        <div className="mb-3">
          <span className="d-block mb-3 fw-bold">Tamaño del Sandwich</span>
          <div className="d-flex justify-content-between">
            {sandwichSizes.map((size) => (
              <>
                <input
                  type="radio"
                  className="btn-check"
                  autoComplete="off"
                  id={`sandwich-size-${size.name}`}
                  name="size"
                  onClick={() => currentSandwichSizeState[1](size.name)}
                />
                <label
                  className={`btn btn-light bg-white text-center ${currentSandwichSizeState[0] === size.name ? 'shadow' : ''}`}
                  htmlFor={`sandwich-size-${size.name}`}
                >
                  <span>{size.name}</span>
                  <img src={SandwichSvg} alt="" className="img-fluid d-block mx-auto" />
                  <span>{size.price}</span>
                </label>
              </>
            ))}
          </div>
        </div>
        <div className="mb-3">
          <span className="d-block mb-3 fw-bold">Extras (Opcional)</span>

        </div>
      </form>
    </div>
  );
}
