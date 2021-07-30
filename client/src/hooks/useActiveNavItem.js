import { useLocation } from 'react-router-dom';

export default function useActiveNavItem() {
  const location = useLocation();

  return {
    active: location.pathname
  };
}
