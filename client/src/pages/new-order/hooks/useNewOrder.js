import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import { useHistory } from 'react-router-dom';
import { Confirm } from 'react-st-modal';

import errorHandler from '../../../utils/errorHandler';
import { api } from '../../../api';

export default function useNewOrder() {
  const history = useHistory();
  const [sandwiches, setSandwiches] = useState([]);
  const [sandwichSizes, setSizes] = useState([]);
  const [sandwichExtras, setExtras] = useState([]);
  const [currentSandwichSize, setCurrentSandwichSize] = useState({});
  const [currentSandwichExtras, setCurrentSandwichExtras] = useState([]);
  const [orderTotal, setOrderTotal] = useState(0);
  const [clientName, setClientName] = useState('');
  const [blockClientName, setBlockClientName] = useState(false);

  const addSandwich = (e) => {
    e.preventDefault();
    let extraPrice = { precio: 0 };

    if (currentSandwichExtras.length) {
      extraPrice = currentSandwichExtras.reduce(
        (prev, current) => ({ precio: prev.precio + current.precio })
      );
    }

    const sandwich = {
      index: sandwiches.length + 1,
      precio: currentSandwichSize.precio + extraPrice.precio,
      size: currentSandwichSize,
      extras: currentSandwichExtras
    };

    setSandwiches([...sandwiches, sandwich]);
    setOrderTotal((prevValue) => prevValue + sandwich.precio);
    setCurrentSandwichSize({});
    setCurrentSandwichExtras([]);
  };

  const addSandwichExtra = (extra) => {
    if (currentSandwichExtras.some((extraItem) => extraItem.codigo === extra.codigo)) {
      setCurrentSandwichExtras(
        currentSandwichExtras.filter((extraItem) => extraItem.codigo !== extra.codigo)
      );
    } else {
      setCurrentSandwichExtras([...currentSandwichExtras, extra]);
    }
  };

  const createOrder = async () => {
    if (!clientName) {
      toast.error('El campo "Nombre de Cliente" es requerido');
      return;
    }

    if (!sandwiches.length) {
      toast.error('La orden no puede estar vacía');
      return;
    }

    const order = {
      cliente: clientName,
      total: orderTotal,
      fecha: new Date(Date.now()),
      sandwiches
    };

    try {
      await api.createOrder(order);

      // Modal de confirmación de agenda de otro pedido
      const result = await Confirm('Su pedido ha sido creado\n¿Desea agendar otro pedido?', 'Pedido Agendado');

      if (result) {
        setClientName('');
        setBlockClientName(false);
        setSandwiches([]);
        setCurrentSandwichSize({});
        setCurrentSandwichExtras([]);
        setOrderTotal(0);
      } else {
        history.push('/home');
      }
    } catch (err) {
      errorHandler(err);
    }
  };

  useEffect(() => {
    (async () => {
      try {
        const sizes = await api.fetchSandwichSizes();
        setSizes(sizes);

        const extras = await api.fetchSandwichesExtras();
        setExtras(extras);
      } catch (err) {
        errorHandler(err);
      }
    })();
  }, []);

  return {
    sandwiches,
    sandwichSizes,
    sandwichExtras,
    currentSandwichSizeState: [currentSandwichSize, setCurrentSandwichSize],
    currentSandwichExtrasState: [currentSandwichExtras, setCurrentSandwichExtras],
    orderTotal,
    clientNameState: [clientName, setClientName],
    blockClientNameState: [blockClientName, setBlockClientName],
    addSandwich,
    addSandwichExtra,
    createOrder
  };
}
