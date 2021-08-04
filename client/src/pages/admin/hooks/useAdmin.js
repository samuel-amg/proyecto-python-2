import { useEffect, useState } from 'react';
import errorHandler from '../../../utils/errorHandler';
import { api } from '../../../api';

export default function useAdmin() {
  const [filterParam, setFilterParam] = useState('');
  const [inputValue, setValue] = useState('');
  const [orders, setOrders] = useState([]);
  const [sizes, setSizes] = useState([]);
  const [extras, setExtras] = useState([]);

  const onChange = (e) => {
    setValue(e.target.value);
  };

  const onChangeFilter = (e) => {
    setFilterParam(e.target.value);
    setValue('');
  };

  const getReport = async () => {
    try {
      const response = await api.fetchReport(filterParam, inputValue);
      setOrders(response);
    } catch (err) {
      errorHandler(err);
    }
  };

  useEffect(() => {
    (async () => {
      try {
        const responseSizes = await api.fetchSandwichSizes();
        setSizes(responseSizes);

        const responseExtras = await api.fetchSandwichesExtras();
        setExtras(responseExtras);

        const responseOrders = await api.fetchReport();
        setOrders(responseOrders);
      } catch (err) {
        errorHandler(err);
      }
    })();
  }, []);

  return {
    filterParam,
    inputValue,
    onChange,
    onChangeFilter,
    getReport,
    orders,
    sizes,
    extras
  };
}
