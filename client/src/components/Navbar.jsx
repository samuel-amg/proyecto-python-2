import Logo from './Logo';
import useActiveNavItem from '../hooks/useActiveNavItem';

export default function Navbar() {
  const { active } = useActiveNavItem();
  return (
    <div className="navbar navbar-expand-lg navbar-dark bg-gunmetal">
      <div className="container-fluid">
        <a href="/" className="navbar-brand">
          <Logo width="120px" height="68px" />
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbar"
          aria-controls="navbar"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon" />
        </button>
        <div className="collapse navbar-collapse" id="navbar">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <a className={`nav-link ${active === '/new-order' ? 'active' : ''}`} aria-current="page" href="/new-order">Nuevo Pedido</a>
            </li>
            <li className="nav-item">
              <a className={`nav-link ${active === '/admin' ? 'active' : ''}`} href="/admin">Administración</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}
