export interface IFilter {
  procedureType?: string[];
  matcher?: string[];
  department?: string[];
}

enum actionTypes {
  SET_FILTERS = "SET_FILTERS",
  CLEAR_FILTERS = "CLEAR_FILTERS",
}

interface IActionProps {
  props: IFilter;
}

interface IAction {
  type: actionTypes;
  payload: IActionProps;
}

interface IDefaultState {
  filters: IFilter;
}

const defaultState: IDefaultState = {
  filters: {},
};

const FilterReducer = (state = defaultState, action: IAction) => {
  switch (action.type) {
    case actionTypes.SET_FILTERS:
      return {
        ...state,
        filters: { ...state.filters, ...action.payload },
      };
    case actionTypes.CLEAR_FILTERS:
      return {
        ...state,
        filters: defaultState.filters,
      };
    default:
      return state;
  }
};

export default FilterReducer;

export const setFilters = (props: IFilter) => {
  return {
    type: actionTypes.SET_FILTERS,
    payload: props,
  };
};

export const clearFilters = () => {
  return {
    type: actionTypes.CLEAR_FILTERS,
  };
};
