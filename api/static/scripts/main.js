// main.js
var app = angular.module('myApp', ['ngGrid']);
app.controller('MyCtrl', function($scope, $http) {

    $scope.skuData = [];
    $scope.loading = true;

    $scope.activateDialogLoading = false;
    $scope.productsDialogLoading = false;
    $scope.validateDialogLoading = false;

    $scope.activateData = '';
    $scope.csvData = '';
    $scope.productsData = '';

    $("#activateDialog").draggable();
    $("#productsDialog").draggable();
    $("#validateDialog").draggable();

    $scope.genericErrorMessage = "An unexpected error has occurred. The requested operation could not be completed.";

    $http.get('/api/products/json').success(function (data) {
        $scope.skuData = data;
        $scope.loading = false;
    }).error(function (data, status, headers, config) {
        alert('error');
    });

    $scope.gridSkus = {
        data: 'skuData',
        //selectedItems: $scope.priceBatchSummaryData,
        multiSelect: false,
        //enablePaging: true,
        enableSorting: true,
        enableColumnResize: true,
        enableColumnReordering: true,
        //showFooter: true,
        //pagingOptions: $scope.pagingOptions,
        columnDefs: [
            { field: 'BrandSlug', width: "100", displayName: 'BrandSlug', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'BundleDescription', width: "200", displayName: 'BundleDescription', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'BundleName', width: "200", displayName: 'BundleName', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'BundleSlug', width: "100", displayName: 'BundleSlug', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'Channel', width: "100", displayName: 'Channel', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'Commodity', width: "100", displayName: 'Commodity', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'DefaultBundle', width: "100", displayName: 'DefaultBundle', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'ECF', width: "50", displayName: 'ECF', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'EffectiveDate', width: "100", displayName: 'EffectiveDate', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'GreenPercentage', width: "100", displayName: 'GreenPercentage', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'LockType', width: "100", displayName: 'LockType', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'Merchandise', width: "100", displayName: 'Merchandise', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'MerchandiseSlug', width: "100", displayName: 'MerchandiseSlug', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'MerchandiseVesting', width: "100", displayName: 'MerchandiseVesting', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'OngoingFrequency', width: "100", displayName: 'OngoingFrequency', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'OngoingValue', width: "100", displayName: 'OngoingValue', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'PartnerCode', width: "100", displayName: 'PartnerCode', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'PremiseType', width: "100", displayName: 'PremiseType', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'PricingTerm', width: "100", displayName: 'PricingTerm', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'PromoCode', width: "100", displayName: 'PromoCode', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'Rate', width: "100", displayName: 'Rate', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'SKU', width: "100", displayName: 'SKU', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'SignupBonus', width: "100", displayName: 'SignupBonus', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'SignupVesting', width: "100", displayName: 'SignupVesting', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'State', width: "60", displayName: 'State', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'Sunday2cents', width: "100", displayName: 'Sunday2cents', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },

            { field: 'TermsOfServiceType', width: "100", displayName: 'TermsOfServiceType', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'UtilityAbbrev', width: "80", displayName: 'UtilityAbbrev', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'UtilityCode', width: "80", displayName: 'UtilityCode', cellTemplate: '<div align="left" style="margin-left: 3px;">{{row.entity[col.field]}}</div>' },
            { field: 'VAS_Code', width: "100", displayName: 'VAS_Code', cellTemplate: '<div align="right" style="margin-right: 3px;">{{row.entity[col.field]}}</div>' }
        ],
    };


    // ------------------ Activate ------------------

    $scope.activate = function () {
        $scope.activateData = '';
        $("#activateDialog").toggle("fast");
    };

    $scope.closeActivateDialog = function () {
        $("#activateDialog").toggle("fast");
    };

    $scope.activatePost = function () {

        $scope.activateDialogLoading = true;

        $http.post('/api/products/activate', $scope.activateData).success(function (data) {
            $scope.activateData = data;
            $scope.activateDialogLoading = false;
        }).error(function (data, status, headers, config) {
            alert('error');
        });
    }

    // ------------------ Products ------------------

    $scope.products = function () {
        $scope.productsData = '';
        $("#productsDialog").toggle("fast");
    };

    $scope.closeProductsDialog = function () {
        $("#productsDialog").toggle("fast");
    };

    $scope.productsPost = function () {

        $scope.productsDialogLoading = true;

        $http.get('/api/products/csv').success(function (data) {
            $scope.productsData = data;
            $scope.productsDialogLoading = false;
        }).error(function (data, status, headers, config) {
            alert('error');
        });
    }

    // ------------------ Validate ------------------

    $scope.validate = function () {
        $scope.csvData = '';
        $("#validateDialog").toggle("fast");
         //$("#validateDialog").dialog('option', 'position', [0,20]);
    }

    $scope.validatePost = function () {

        $scope.validateDialogLoading = true;

        $http.post('/api/products/validate', $scope.csvData).success(function (data) {
            $scope.csvData = data;
            $scope.validateDialogLoading = false;
        }).error(function (data, status, headers, config) {
            alert('error');
        });
    }


    $scope.closeValidateDialog = function () {
        //$scope.createPriceBatchButtonDisabled = false;
        //$scope.meterReadDate = "";
        //$scope.setDialogButtonDisabledState(false);
        $("#validateDialog").toggle("fast");
    };


});
