import PropTypes from 'prop-types';

import { ReactComponent as LogoSvg } from '../assets/logo-large.svg';

export default function Logo({
  width = '100px',
  height = '50px',
  ...props
}) {
  return (
    <div style={{ width, height }} {...props}>
      <LogoSvg className="align-top h-100 w-100" />
    </div>
  );
}

Logo.propTypes = {
  width: PropTypes.string,
  height: PropTypes.string
};
