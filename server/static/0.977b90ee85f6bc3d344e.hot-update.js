webpackHotUpdate(0,{

/***/ 979:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});

var _jsx = function () { var REACT_ELEMENT_TYPE = typeof Symbol === "function" && Symbol.for && Symbol.for("react.element") || 0xeac7; return function createRawReactElement(type, props, key, children) { var defaultProps = type && type.defaultProps; var childrenLength = arguments.length - 3; if (!props && childrenLength !== 0) { props = {}; } if (props && defaultProps) { for (var propName in defaultProps) { if (props[propName] === void 0) { props[propName] = defaultProps[propName]; } } } else if (!props) { props = defaultProps || {}; } if (childrenLength === 1) { props.children = children; } else if (childrenLength > 1) { var childArray = Array(childrenLength); for (var i = 0; i < childrenLength; i++) { childArray[i] = arguments[i + 3]; } props.children = childArray; } return { $$typeof: REACT_ELEMENT_TYPE, type: type, key: key === undefined ? null : '' + key, ref: null, props: props, _owner: null }; }; }();

var _react = __webpack_require__(0);

var _react2 = _interopRequireDefault(_react);

var _reactRouterDom = __webpack_require__(184);

var _PageRoot = __webpack_require__(980);

var _PageRoot2 = _interopRequireDefault(_PageRoot);

var _ReportPage = __webpack_require__(983);

var _ReportPage2 = _interopRequireDefault(_ReportPage);

var _SettingsPage = __webpack_require__(1323);

var _SettingsPage2 = _interopRequireDefault(_SettingsPage);

var _ImageAnalysisPage = __webpack_require__(1324);

var _ImageAnalysisPage2 = _interopRequireDefault(_ImageAnalysisPage);

var _ModalRouter = __webpack_require__(1359);

var _ModalRouter2 = _interopRequireDefault(_ModalRouter);

var _ModalRoute = __webpack_require__(1360);

var _ModalRoute2 = _interopRequireDefault(_ModalRoute);

var _AttachImageModal = __webpack_require__(1361);

var _AttachImageModal2 = _interopRequireDefault(_AttachImageModal);

var _Sidebar = __webpack_require__(1363);

var _Sidebar2 = _interopRequireDefault(_Sidebar);

__webpack_require__(1368);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var _ref = _jsx(_Sidebar2.default, {});

var _ref2 = _jsx(_ModalRouter2.default, {}, void 0, _jsx(_ModalRoute2.default, {
    name: 'attachImage',
    component: _AttachImageModal2.default
}));

var _ref3 = _jsx(_reactRouterDom.Route, {
    exact: true,
    path: '/',
    component: _ImageAnalysisPage2.default
});

var _ref4 = _jsx(_reactRouterDom.Route, {
    path: '/image',
    component: _ImageAnalysisPage2.default
});

var _ref5 = _jsx(_reactRouterDom.Route, {
    path: '/report',
    component: _ReportPage2.default
});

var App = function App() {
    return _jsx('div', {
        className: 'app'
    }, void 0, _ref, _ref2, _jsx(_PageRoot2.default, {}, void 0, _jsx(_reactRouterDom.Switch, {}, void 0, _ref3, _ref4, _ref5)));
};

exports.default = App;

/***/ })

})
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi93ZWJhcHAvY29tcG9uZW50cy9hcHAvQXBwLmpzIl0sIm5hbWVzIjpbIkFwcCJdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7OztBQUNBOztBQUVBOzs7O0FBQ0E7Ozs7QUFDQTs7OztBQUNBOzs7O0FBRUE7Ozs7QUFDQTs7OztBQUNBOzs7O0FBRUE7Ozs7QUFFQTs7Ozs7OztVQU02QixhOzs7Ozs7VUFJSyxHOzs7OztVQUNOLFE7Ozs7O1VBQ0EsUzs7OztBQVY1QixJQUFNQSxNQUFNLFNBQU5BLEdBQU07QUFBQTtBQUFBLG1CQUNPO0FBRFA7QUFBQSxDQUFaOztrQkFnQmVBLEciLCJmaWxlIjoiMC45NzdiOTBlZTg1ZjZiYzNkMzQ0ZS5ob3QtdXBkYXRlLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IFJlYWN0LCB7IENvbXBvbmVudCB9IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IFJvdXRlLCBTd2l0Y2ggfSBmcm9tICdyZWFjdC1yb3V0ZXItZG9tJztcblxuaW1wb3J0IFBhZ2VSb290IGZyb20gJ3BhZ2VzL1BhZ2VSb290JztcbmltcG9ydCBSZXBvcnRQYWdlIGZyb20gJ3BhZ2VzL1JlcG9ydFBhZ2UnO1xuaW1wb3J0IFNldHRpbmdzUGFnZSBmcm9tICdwYWdlcy9TZXR0aW5nc1BhZ2UnO1xuaW1wb3J0IEltYWdlQW5hbHlzaXNQYWdlIGZyb20gJ3BhZ2VzL0ltYWdlQW5hbHlzaXNQYWdlJztcblxuaW1wb3J0IE1vZGFsUm91dGVyIGZyb20gJ2NvbXBvbmVudHMvbW9kYWwvTW9kYWxSb3V0ZXInO1xuaW1wb3J0IE1vZGFsUm91dGUgZnJvbSAnY29tcG9uZW50cy9tb2RhbC9Nb2RhbFJvdXRlJztcbmltcG9ydCBBdHRhY2hJbWFnZU1vZGFsIGZyb20gJ2NvbXBvbmVudHMvbW9kYWwvQXR0YWNoSW1hZ2VNb2RhbCc7XG5cbmltcG9ydCBTaWRlYmFyIGZyb20gJ2NvbXBvbmVudHMvc2lkZWJhci9TaWRlYmFyJztcblxuaW1wb3J0ICdzdHlsZS9hcHAvQXBwLnNjc3MnO1xuXG5jb25zdCBBcHAgPSAoKSA9PlxuICAgIDxkaXYgY2xhc3NOYW1lPVwiYXBwXCIgPlxuICAgICAgICA8U2lkZWJhciAvPlxuICAgICAgICA8TW9kYWxSb3V0ZXI+XG4gICAgICAgICAgICA8TW9kYWxSb3V0ZSBuYW1lPSdhdHRhY2hJbWFnZScgY29tcG9uZW50PXtBdHRhY2hJbWFnZU1vZGFsfS8+XG4gICAgICAgIDwvTW9kYWxSb3V0ZXI+XG4gICAgICAgIDxQYWdlUm9vdD5cbiAgICAgICAgICAgIDxTd2l0Y2g+XG4gICAgICAgICAgICAgICAgPFJvdXRlIGV4YWN0IHBhdGg9XCIvXCIgY29tcG9uZW50PXtJbWFnZUFuYWx5c2lzUGFnZX0gLz5cbiAgICAgICAgICAgICAgICA8Um91dGUgcGF0aD1cIi9pbWFnZVwiIGNvbXBvbmVudD17SW1hZ2VBbmFseXNpc1BhZ2V9IC8+XG4gICAgICAgICAgICAgICAgPFJvdXRlIHBhdGg9XCIvcmVwb3J0XCIgY29tcG9uZW50PXtSZXBvcnRQYWdlfSAvPlxuICAgICAgICAgICAgICAgIHsvKiA8Um91dGUgcGF0aD1cIi9zZXR0aW5nc1wiIGNvbXBvbmVudD17U2V0dGluZ3NQYWdlfSAvPiAqL31cbiAgICAgICAgICAgIDwvU3dpdGNoPlxuICAgICAgICA8L1BhZ2VSb290PlxuICAgIDwvZGl2PlxuXG5leHBvcnQgZGVmYXVsdCBBcHA7XG5cblxuLy8gV0VCUEFDSyBGT09URVIgLy9cbi8vIC4vd2ViYXBwL2NvbXBvbmVudHMvYXBwL0FwcC5qcyJdLCJzb3VyY2VSb290IjoiIn0=