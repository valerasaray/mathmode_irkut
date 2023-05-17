CREATE MIGRATION m1i4x5hcbgelddjsmemvmimecl67hcxpr3gmplla2qvb6gufbeyj6a
    ONTO m1islthvxb7eexwclxkvem6abormpni6xsxwxaqy72pxntqciv3uxa
{
  ALTER TYPE default::Notification {
      ALTER LINK passed_node {
          SET MULTI;
      };
  };
};
