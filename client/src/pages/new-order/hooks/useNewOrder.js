import { useEffect, useState } from 'react';

import { SandwichSizes } from '../../../mocks';
import errorHandler from '../../../utils/errorHandler';
import { api } from '../../../api';

export default function useNewOrder() {
  const [step, setStep] = useState(1);
  const [orders, setOrders] = useState([]);
  const [currentOrder, setCurrentOrder] = useState({});
  const [sandwiches, setSandwiches] = useState([]);
  const [sandwichSizes, setSizes] = useState([]);
  const [sandwichExtras, setExtras] = useState([]);
  const [currentSandwichSize, setCurrentSandwichSize] = useState('');
  const [currentSandwichExtras, setCurrentSandwichExtras] = useState([]);
  const [orderTotal, setOrderTotal] = useState(0);
  const [clientName, setClientName] = useState('');
  const [blockClientName, setBlockClientName] = useState(false);

  const addSandwich = (sandwich) => {
    setSandwiches((prevValues) => [...prevValues, sandwich]);
    setOrderTotal((prevValue) => prevValue + sandwich.price);
    setCurrentSandwichSize('');
    setCurrentSandwichExtras([]);
  };

  useEffect(() => {
    (async () => {
      try {
        const sizes = SandwichSizes;
        setSizes(sizes);

        const extras = await api.fetchSandwichesExtras();
        setExtras(extras);
      } catch (err) {
        errorHandler(err);
      }
    })();
  }, []);

  return {
    stepState: [step, setStep],
    sandwiches,
    sandwichSizes,
    sandwichExtras,
    currentSandwichSizeState: [currentSandwichSize, setCurrentSandwichSize],
    currentSandwichExtrasState: [currentSandwichExtras, setCurrentSandwichExtras],
    ordersState: [orders, setOrders],
    currentOrderState: [currentOrder, setCurrentOrder],
    orderTotal,
    clientNameState: [clientName, setClientName],
    blockClientNameState: [blockClientName, setBlockClientName],
    addSandwich
  };
}
