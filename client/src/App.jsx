import React from 'react';
import {
  BrowserRouter,
  Switch,
  Route
} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';

import Navbar from './components/Navbar';
import HomeRoute from './pages/home/HomeRoute';
import NewOrderRoute from './pages/new-order/NewOrderRoute';
import AdminRoute from './pages/admin/AdminRoute';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container-fluid">
        <Switch>
          <Route exact path="/new-order" component={NewOrderRoute} />
          <Route exact path="/admin" component={AdminRoute} />
          <Route path="/" component={HomeRoute} />
        </Switch>
      </div>
      <ToastContainer />
    </BrowserRouter>
  );
}
