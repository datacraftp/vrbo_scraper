import json

payload_data = json.dumps([
  {
    "operationName": "PropertySearchDynamicSearchMapQuery",
    "variables": {
      "returnPropertyType": True,
      "criteria": {
        "primary": {
          "dateRange": {
            "checkInDate": {
              "day": 13,
              "month": 9,
              "year": 2023
            },
            "checkOutDate": {
              "day": 14,
              "month": 9,
              "year": 2023
            }
          },
          "destination": {
            "regionName": None,
            # "regionId": "2621",
            "coordinates": None,
            "pinnedPropertyId": None,
            "propertyIds": None,
            "mapBounds": None
          },
          "rooms": [
            {
              "adults": 1,
              "children": []
            }
          ]
        },
        "secondary": {
          "counts": [
            {
              "id": "resultsStartingIndex",
              "value": 0
            },
            {
              "id": "resultsSize",
              "value": 50
            }
          ],
          "booleans": [],
          "selections": [
            {
              "id": "sort",
              "value": "RECOMMENDED"
            },
            {
              "id": "privacyTrackingState",
              "value": "CAN_NOT_TRACK"
            },
            {
              "id": "useRewards",
              "value": "SHOP_WITHOUT_POINTS"
            }
          ],
          "ranges": []
        }
      },
      "destination": {
        "regionName": None,
        "regionId": None,
        "coordinates": None,
        "pinnedPropertyId": None,
        "propertyIds": None,
        "mapBounds": None
      },
      "shoppingContext": {
        "multiItem": None
      },
      "context": {
        "siteId": 9001001,
        "locale": "en_US",
        "eapid": 1,
        "currency": "USD",
        "device": {
          "type": "DESKTOP"
        },
        "identity": {
          "duaid": "01a3e1bf-eaf5-c562-a72b-ed1f1aebf5dc",
          "expUserId": "-1",
          "tuid": "-1",
          "authState": "ANONYMOUS"
        },
        "privacyTrackingState": "CAN_TRACK",
        "debugContext": {
          "abacusOverrides": [],
          "alterMode": "RELEASED"
        }
      }
    },
    "query": "query PropertySearchDynamicSearchMapQuery($context: ContextInput!, $destination: DestinationInput!, $rooms: [RoomInput!], $dateRange: PropertyDateRangeInput, $sort: PropertySort, $filters: PropertySearchFiltersInput, $marketing: PropertyMarketingInfoInput, $propertyShopOptions: PropertyShopOptionsInput, $searchPagination: PaginationInput, $searchIntent: SearchIntentInput, $shoppingContext: ShoppingContextInput, $criteria: PropertySearchCriteriaInput, $returnPropertyType: Boolean = true) {\n  propertySearch(\n    context: $context\n    destination: $destination\n    rooms: $rooms\n    dateRange: $dateRange\n    sort: $sort\n    filters: $filters\n    marketing: $marketing\n    propertyShopOptions: $propertyShopOptions\n    searchPagination: $searchPagination\n    searchIntent: $searchIntent\n    shoppingContext: $shoppingContext\n    criteria: $criteria\n    returnPropertyType: $returnPropertyType\n  ) {\n    dynamicMap {\n      mapToolbar {\n        ...MapToolbarFragment\n        __typename\n      }\n      autoSearchOnMapMove {\n        ...LodgingEGDSCheckboxFragment\n        __typename\n      }\n      action {\n        ...LodgingEGDSFloatingActionButtonFragment\n        __typename\n      }\n      adaptExSuccessEvents {\n        ...LodgingAdaptExAnalyticsEventFragment\n        __typename\n      }\n      filterPlacement\n      map {\n        ...DynamicMapFragment\n        __typename\n      }\n      __typename\n    }\n    propertySearchListings {\n      ...LodgingCardFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LodgingAdaptExAnalyticsEventFragment on LodgingAdaptExAnalyticsEvent {\n  campaignId\n  clientSideAnalytics {\n    referrerId\n    eventType\n    linkName\n    __typename\n  }\n  events {\n    eventType\n    eventTarget\n    banditDisplayed\n    payloadId\n    __typename\n  }\n  __typename\n}\n\nfragment MapToolbarFragment on MapToolbar {\n  title\n  subtitle\n  __typename\n}\n\nfragment ClientSideAnalyticsFragment on ClientSideAnalytics {\n  eventType\n  linkName\n  referrerId\n  uisPrimeMessages {\n    schemaName\n    messageContent\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingEGDSIconFragment on Icon {\n  description\n  id\n  size\n  theme\n  __typename\n}\n\nfragment LodgingUILinkActionFragment on UILinkAction {\n  resource {\n    ... on HttpURI {\n      relativePath\n      value\n      __typename\n    }\n    __typename\n  }\n  target\n  useRelativePath\n  __typename\n}\n\nfragment LodgingEGDSFloatingActionButtonFragment on UIPrimaryButton {\n  accessibility\n  analytics {\n    ...ClientSideAnalyticsFragment\n    __typename\n  }\n  disabled\n  primary\n  action {\n    ...LodgingUILinkActionFragment\n    __typename\n  }\n  icon {\n    ...LodgingEGDSIconFragment\n    __typename\n  }\n  egdsElementId\n  __typename\n}\n\nfragment LodgingEGDSCheckboxFragment on EGDSBasicCheckBox {\n  ...LodgingEGDSBasicCheckBoxFragment\n  __typename\n}\n\nfragment LodgingEGDSBasicCheckBoxFragment on EGDSBasicCheckBox {\n  egdsElementId\n  description\n  enabled\n  checkedAnalytics {\n    linkName\n    referrerId\n    __typename\n  }\n  uncheckedAnalytics {\n    linkName\n    referrerId\n    __typename\n  }\n  label {\n    text\n    __typename\n  }\n  name\n  required\n  state\n  __typename\n}\n\nfragment DynamicMapFragment on EGDSBasicMap {\n  label\n  initialViewport\n  center {\n    latitude\n    longitude\n    __typename\n  }\n  zoom\n  bounds {\n    northeast {\n      latitude\n      longitude\n      __typename\n    }\n    southwest {\n      latitude\n      longitude\n      __typename\n    }\n    __typename\n  }\n  computedBoundsOptions {\n    coordinates {\n      latitude\n      longitude\n      __typename\n    }\n    gaiaId\n    lowerQuantile\n    upperQuantile\n    marginMultiplier\n    minMargin\n    minimumPins\n    interpolationRatio\n    __typename\n  }\n  config {\n    ... on EGDSDynamicMapConfig {\n      accessToken\n      egdsMapProvider\n      externalConfigEndpoint {\n        value\n        __typename\n      }\n      mapId\n      __typename\n    }\n    __typename\n  }\n  markers {\n    ... on EGDSMapFeature {\n      id\n      description\n      markerPosition {\n        latitude\n        longitude\n        __typename\n      }\n      type\n      markerStatus\n      qualifiers\n      text\n      clientSideAnalytics {\n        linkName\n        referrerId\n        __typename\n      }\n      onSelectAccessibilityMessage\n      onEnterAccessibilityMessage\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardFragment on LodgingCard {\n  featuredHeader {\n    header {\n      text\n      __typename\n    }\n    __typename\n  }\n  cardLink {\n    ...LodgingCardLinkFragment\n    __typename\n  }\n  footerActions {\n    ...LodgingCardLinkActionFragment\n    __typename\n  }\n  mediaSection {\n    ...LodgingCardMediaSectionFragment\n    __typename\n  }\n  id\n  ...LodgingCardContentSectionFragment\n  clickstreamEvents {\n    productPresented {\n      ...ProductEventFragment\n      __typename\n    }\n    productSelected {\n      ...ProductEventFragment\n      __typename\n    }\n    __typename\n  }\n  impressionAnalytics {\n    url\n    referrerId\n    linkName\n    uisPrimeMessages {\n      messageContent\n      schemaName\n      __typename\n    }\n    __typename\n  }\n  adaptexSuccessActionTracking {\n    ...AdaptexCampaignTrackingDetailFragment\n    __typename\n  }\n  __typename\n}\n\nfragment ProductEventFragment on LodgingProductEvent {\n  event {\n    ...ClickstreamEventFragment\n    __typename\n  }\n  product_list {\n    ...ProductListFragment\n    __typename\n  }\n  search_request {\n    ...RequestFragment\n    __typename\n  }\n  __typename\n}\n\nfragment ClickstreamEventFragment on EGClickstreamEvent {\n  eventCategory\n  eventName\n  eventType\n  eventVersion\n  __typename\n}\n\nfragment ProductListFragment on LodgingProduct {\n  product_id\n  __typename\n}\n\nfragment RequestFragment on LodgingSearchRequest {\n  search_id\n  __typename\n}\n\nfragment LodgingCardLinkActionFragment on LodgingCardLinkAction {\n  link {\n    text\n    action {\n      target\n      resource {\n        ... on HttpURI {\n          value\n          relativePath\n          __typename\n        }\n        __typename\n      }\n      useRelativePath\n      analytics {\n        referrerId\n        linkName\n        __typename\n      }\n      __typename\n    }\n    icon {\n      id\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardMediaSectionFragment on LodgingCardMediaSection {\n  gallery {\n    ...LodgingGalleryCarouselFragment\n    __typename\n  }\n  saveItem {\n    ...LodgingCardSaveItemFragment\n    __typename\n  }\n  saveTripItem {\n    ...TripsSaveItemFragment\n    __typename\n  }\n  badges {\n    primaryBadge {\n      ...LodgingBadgeFragment\n      __typename\n    }\n    secondaryBadge {\n      ...LodgingBadgeFragment\n      __typename\n    }\n    tertiaryBadge {\n      ...LodgingBadgeFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingBadgeFragment on EGDSStandardBadge {\n  text\n  theme\n  graphic {\n    __typename\n    ... on Icon {\n      description\n      id\n      __typename\n    }\n    ... on Mark {\n      description\n      id\n      __typename\n    }\n  }\n  size\n  __typename\n}\n\nfragment LodgingGalleryCarouselFragment on LodgingGalleryCarousel {\n  accessibilityHeadingText\n  navClickAnalytics {\n    referrerId\n    linkName\n    __typename\n  }\n  intersectionAnalytics {\n    referrerId\n    linkName\n    uisPrimeMessages {\n      messageContent\n      schemaName\n      __typename\n    }\n    __typename\n  }\n  media {\n    ...LodgingMediaItemFragment\n    __typename\n  }\n  nextButtonText\n  previousButtonText\n  __typename\n}\n\nfragment LodgingMediaItemFragment on LodgingMediaItem {\n  id\n  media {\n    ... on Image {\n      ...LodgingEGDSImageFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingEGDSImageFragment on Image {\n  description\n  url\n  thumbnailClickAnalytics {\n    referrerId\n    linkName\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardSaveItemFragment on LodgingSaveItem {\n  items {\n    itemId\n    __typename\n  }\n  labels {\n    saveLabel\n    removeLabel\n    __typename\n  }\n  messages {\n    saveMessage\n    removeMessage\n    __typename\n  }\n  initialChecked\n  analytics {\n    linkName\n    referrerId\n    __typename\n  }\n  __typename\n}\n\nfragment TripsSaveItemFragment on TripsSaveItem {\n  initialChecked\n  itemId\n  source\n  attributes {\n    ...TripsSaveStayAttributesFragment\n    ...TripsSaveActivityAttributesFragment\n    __typename\n  }\n  save {\n    ...TripsSaveItemPropertiesFragment\n    __typename\n  }\n  remove {\n    ...TripsSaveItemPropertiesFragment\n    __typename\n  }\n  __typename\n}\n\nfragment TripsSaveStayAttributesFragment on TripsSaveStayAttributes {\n  checkInDate {\n    ...DateFragment\n    __typename\n  }\n  checkoutDate {\n    ...DateFragment\n    __typename\n  }\n  regionId\n  roomConfiguration {\n    numberOfAdults\n    childAges\n    __typename\n  }\n  __typename\n}\n\nfragment TripsSaveActivityAttributesFragment on TripsSaveActivityAttributes {\n  regionId\n  dateRange {\n    start {\n      ...DateFragment\n      __typename\n    }\n    end {\n      ...DateFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TripsSaveItemPropertiesFragment on TripsSaveItemProperties {\n  accessibility\n  analytics {\n    referrerId\n    linkName\n    uisPrimeMessages {\n      messageContent\n      schemaName\n      __typename\n    }\n    __typename\n  }\n  adaptexSuccessCampaignIds {\n    ...AdaptexCampaignTrackingDetailFragment\n    __typename\n  }\n  label\n  __typename\n}\n\nfragment DateFragment on Date {\n  day\n  month\n  year\n  __typename\n}\n\nfragment AdaptexCampaignTrackingDetailFragment on AdaptexCampaignTrackingDetail {\n  campaignId\n  eventTarget\n  __typename\n}\n\nfragment LodgingCardHeadingSectionFragment on LodgingCardHeadingSection {\n  heading\n  productRating {\n    ...LodgingEGDSRatingFragment\n    __typename\n  }\n  featuredMessages {\n    ...LodgingCardFeaturedMessageFragment\n    __typename\n  }\n  messages {\n    ...LodgingEGDSTextFragment\n    __typename\n  }\n  amenities {\n    ...LodgingProductAmenityFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingEGDSRatingFragment on EGDSRating {\n  accessibility\n  rating\n  ... on EGDSIconRating {\n    icon {\n      id\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardFeaturedMessageFragment on LodgingCardFeaturedMessage {\n  icon {\n    id\n    description\n    size\n    __typename\n  }\n  text\n  __typename\n}\n\nfragment LodgingEGDSTextFragment on EGDSText {\n  ... on EGDSParagraph {\n    ...LodgingEGDSParagraphFragment\n    __typename\n  }\n  ... on EGDSStylizedText {\n    ...EGDSStylizedTextFragment\n    __typename\n  }\n  ... on EGDSPlainText {\n    __typename\n    text\n  }\n  ... on EGDSInlineLink {\n    ...LodgingEGDSInlineLinkFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingEGDSParagraphFragment on EGDSParagraph {\n  __typename\n  text\n}\n\nfragment EGDSStylizedTextFragment on EGDSStylizedText {\n  __typename\n  text\n  theme\n  weight\n  size\n  decorative\n  accessibility\n}\n\nfragment LodgingEGDSInlineLinkFragment on EGDSInlineLink {\n  action {\n    accessibility\n    analytics {\n      linkName\n      referrerId\n      __typename\n    }\n    resource {\n      value\n      __typename\n    }\n    target\n    __typename\n  }\n  disabled\n  linkSize: size\n  text\n  __typename\n}\n\nfragment LodgingProductAmenityFragment on EGDSIconText {\n  icon {\n    ...LodgingEGDSIconFragment\n    __typename\n  }\n  text\n  __typename\n}\n\nfragment LodgingCardContentSectionFragment on LodgingCard {\n  __typename\n  headingSection {\n    ...LodgingCardHeadingSectionFragment\n    __typename\n  }\n  summarySections {\n    ...LodgingCardProductSummarySectionFragment\n    __typename\n  }\n  priceSection {\n    priceSummary {\n      ...PriceSummaryFragment\n      marketingFeeDetails {\n        ...LodgingCardMarketingFeeDetailFragment\n        __typename\n      }\n      __typename\n    }\n    badge {\n      ...LodgingBadgeFragment\n      __typename\n    }\n    standardBadge {\n      ...LodgingStandardBadgeFragment\n      __typename\n    }\n    button {\n      accessibility\n      action {\n        analytics {\n          linkName\n          referrerId\n          __typename\n        }\n        resource {\n          value\n          __typename\n        }\n        __typename\n      }\n      analytics {\n        linkName\n        referrerId\n        __typename\n      }\n      disabled\n      icon {\n        description\n        id\n        __typename\n      }\n      primary\n      attemptEvents {\n        ...LodgingAdaptExAnalyticsEventFragment\n        __typename\n      }\n      successEvents {\n        ...LodgingAdaptExAnalyticsEventFragment\n        __typename\n      }\n      adaptexSuccessActionTracking {\n        ...AdaptexCampaignTrackingDetailFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  compareSection {\n    ...LodgingCardCompareSectionFragment\n    __typename\n  }\n  dateSection {\n    ...LodgingCardDateSectionFragment\n    __typename\n  }\n  callOut {\n    ...LodgingEGDSTextFragment\n    __typename\n  }\n  id\n}\n\nfragment LodgingCardProductSummarySectionFragment on LodgingCardProductSummarySection {\n  heading {\n    ...LodgingEGDSHeadingFragment\n    __typename\n  }\n  amenities {\n    ...LodgingProductAmenityFragment\n    __typename\n  }\n  messages {\n    ...LodgingEGDSTextFragment\n    __typename\n  }\n  descriptionSection {\n    ...LodgingCardPropertyDescriptionSectionFragment\n    __typename\n  }\n  changeActionDialog {\n    ...LodgingCardChangeUnitDialogActionFragment\n    __typename\n  }\n  changeActionSheet {\n    ...LodgingCardChangeUnitSheetActionFragment\n    __typename\n  }\n  detailsAction {\n    ...LodgingCardPropertyDialogActionFragment\n    __typename\n  }\n  guestRating {\n    ...LodgingCardGuestRatingFragment\n    __typename\n  }\n  footerMessages {\n    listItems {\n      ...LodgingProductFooterMessagesFragment\n      ...LodgingProductSpannableFooterMessagesFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingEGDSHeadingFragment on EGDSHeading {\n  __typename\n  text\n}\n\nfragment LodgingCardPropertyDescriptionSectionFragment on LodgingCardPropertyDescriptionSection {\n  heading {\n    text\n    __typename\n  }\n  description {\n    text\n    __typename\n  }\n  link {\n    action {\n      resource {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardChangeUnitDialogActionFragment on LodgingCardChangeUnitDialogAction {\n  dialog {\n    closeAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    toolbar {\n      ...EGDSDialogToolbarFragment\n      __typename\n    }\n    __typename\n  }\n  trigger {\n    ...LodgingCardMoreDetailsTriggerFragment\n    __typename\n  }\n  __typename\n}\n\nfragment EGDSDialogToolbarFragment on EGDSDialogToolbar {\n  closeText\n  title\n  __typename\n}\n\nfragment LodgingCardMoreDetailsTriggerFragment on LodgingCardMoreDetailsTrigger {\n  accessibilityLabel\n  analytics {\n    linkName\n    referrerId\n    __typename\n  }\n  icon {\n    ...LodgingEGDSIconFragment\n    __typename\n  }\n  label\n  __typename\n}\n\nfragment LodgingCardChangeUnitSheetActionFragment on LodgingCardChangeUnitSheetAction {\n  sheet {\n    closeAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    closeText\n    __typename\n  }\n  trigger {\n    ...LodgingCardMoreDetailsTriggerFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardPropertyDialogActionFragment on LodgingCardDetailsAction {\n  __typename\n  ... on LodgingCardUnitDetailsDialog {\n    ...LodgingCardUnitDetailsDialogActionFragment\n    __typename\n  }\n  ... on LodgingCardPropertyDetailsDialog {\n    ...LodgingCardPropertyDetailsDialogActionFragment\n    __typename\n  }\n}\n\nfragment LodgingCardPropertyDetailsDialogActionFragment on LodgingCardPropertyDetailsDialog {\n  dialog {\n    closeAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    toolbar {\n      ...EGDSDialogToolbarFragment\n      __typename\n    }\n    __typename\n  }\n  trigger {\n    ...LodgingCardMoreDetailsLinkTriggerFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardMoreDetailsLinkTriggerFragment on LodgingCardMoreDetailsTrigger {\n  accessibilityLabel\n  analytics {\n    linkName\n    referrerId\n    __typename\n  }\n  icon {\n    ...LodgingEGDSIconFragment\n    __typename\n  }\n  label\n  __typename\n}\n\nfragment LodgingCardUnitDetailsDialogActionFragment on LodgingCardUnitDetailsDialog {\n  dialog {\n    closeAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    toolbar {\n      ...EGDSDialogToolbarFragment\n      __typename\n    }\n    __typename\n  }\n  trigger {\n    ...LodgingCardMoreDetailsLinkTriggerFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardGuestRatingFragment on LodgingCardPhrase {\n  accessibilityLabel\n  phraseParts {\n    ...EGDSIconRatingFragment\n    __typename\n  }\n  parts {\n    text\n    ... on EGDSStylizedText {\n      ...EGDSStylizedTextFragment\n      __typename\n    }\n    ... on EGDSText {\n      ...LodgingEGDSTextFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EGDSIconRatingFragment on EGDSIconRating {\n  rating\n  icon {\n    size\n    theme\n    token\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingProductFooterMessagesFragment on EGDSTextWithMarkListItem {\n  mark {\n    description\n    id\n    url {\n      value\n      __typename\n    }\n    __typename\n  }\n  egdsElementId\n  style\n  text\n  __typename\n}\n\nfragment LodgingProductSpannableFooterMessagesFragment on EarnMessageContainerListItem {\n  graphic {\n    ... on Mark {\n      description\n      id\n      token\n      url {\n        value\n        relativePath\n        __typename\n      }\n      __typename\n    }\n    ... on Icon {\n      description\n      id\n      size\n      theme\n      title\n      __typename\n    }\n    ... on Illustration {\n      id\n      description\n      __typename\n    }\n    __typename\n  }\n  style\n  text\n  stylizedText {\n    ... on EGDSSpannableText {\n      text\n      contents {\n        ... on EGDSPlainText {\n          text\n          __typename\n        }\n        ... on EGDSStylizedText {\n          text\n          theme\n          weight\n          size\n          decorative\n          accessibility\n          __typename\n        }\n        __typename\n      }\n      inlineContent {\n        ... on EGDSPlainText {\n          text\n          __typename\n        }\n        ... on EGDSStylizedText {\n          text\n          theme\n          weight\n          size\n          decorative\n          accessibility\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceSummaryFragment on PropertyPrice {\n  displayMessages {\n    lineItems {\n      ...PriceMessageFragment\n      ...EnrichedMessageFragment\n      __typename\n    }\n    __typename\n  }\n  options {\n    leadingCaption\n    displayPrice {\n      formatted\n      __typename\n    }\n    disclaimer {\n      value\n      __typename\n    }\n    priceDisclaimer {\n      content\n      primaryButton {\n        text\n        __typename\n      }\n      trigger {\n        icon {\n          description\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    accessibilityLabel\n    strikeOut {\n      formatted\n      __typename\n    }\n    loyaltyPrice {\n      unit\n      amount {\n        formatted\n        __typename\n      }\n      totalStrikeOutPoints {\n        formatted\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  priceMessaging {\n    value\n    theme\n    __typename\n  }\n  __typename\n}\n\nfragment PriceMessageFragment on DisplayPrice {\n  __typename\n  role\n  price {\n    formatted\n    accessibilityLabel\n    __typename\n  }\n  disclaimer {\n    content\n    primaryUIButton {\n      accessibility\n      primary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment EnrichedMessageFragment on LodgingEnrichedMessage {\n  __typename\n  value\n  state\n}\n\nfragment LodgingCardMarketingFeeDetailFragment on MarketingFeeDetails {\n  tierMessage {\n    accessibilityLabel\n    value\n    egdsMark {\n      id\n      __typename\n    }\n    __typename\n  }\n  marketingFeeMessageDialog {\n    content\n    dialog {\n      footer {\n        buttons {\n          primary\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardCompareSectionFragment on LodgingCardCompareSection {\n  __typename\n  compareAction {\n    ... on EGDSBasicCheckBox {\n      __typename\n      label {\n        text\n        __typename\n      }\n    }\n    __typename\n  }\n}\n\nfragment LodgingCardDateSectionFragment on LodgingCardDateSection {\n  date {\n    ...EGDSStylizedTextFragment\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingStandardBadgeFragment on LodgingStandardBadge {\n  standardBadge {\n    text\n    theme\n    graphic {\n      __typename\n      ... on Icon {\n        description\n        id\n        __typename\n      }\n      ... on Mark {\n        description\n        id\n        __typename\n      }\n    }\n    size\n    __typename\n  }\n  impressionEventAnalytics {\n    referrerId\n    linkName\n    event\n    __typename\n  }\n  __typename\n}\n\nfragment LodgingCardLinkFragment on UILinkAction {\n  __typename\n  accessibility\n  resource {\n    __typename\n    ... on HttpURI {\n      relativePath\n      value\n      __typename\n    }\n  }\n  analytics {\n    linkName\n    referrerId\n    uisPrimeMessages {\n      messageContent\n      schemaName\n      __typename\n    }\n    __typename\n  }\n  useRelativePath\n  target\n}\n"
  }
])

payload_comments = json.dumps([
  {
    "operationName": "PropertyFilteredReviewsQuery",
    "variables": {
      "context": {
        "siteId": 9001001,
        "locale": "en_US",
        "eapid": 1,
        "currency": "USD",
        "device": {
          "type": "DESKTOP"
        },
        "identity": {
          "duaid": "01a3e3cf-eaf5-c462-a78b-ed4f4aebf5dc",
          "expUserId": "-1",
          "tuid": "-1",
          "authState": "ANONYMOUS"
        },
        "privacyTrackingState": "CAN_TRACK",
        "debugContext": {
          "abacusOverrides": [],
          "alterMode": "RELEASED"
        }
      },
      "propertyId": None,
      "searchCriteria": {
        "primary": {
          "dateRange": None,
          "rooms": [
            {
              "adults": 2
            }
          ],
          "destination": {
            "regionId": "178293"
          }
        },
        "secondary": {
          "booleans": [
            {
              "id": "includeRecentReviews",
              "value": True
            },
            {
              "id": "includeRatingsOnlyReviews",
              "value": True
            },
            {
              "id": "overrideEmbargoForIndividualReviews",
              "value": True
            }
          ],
          "counts": [
            {
              "id": "startIndex",
              "value": 0
            },
            {
              "id": "size",
              "value": 100
            }
          ],
          "selections": [
            {
              "id": "sortBy",
              "value": "NEWEST_TO_OLDEST_BY_LANGUAGE"
            }
          ]
        }
      }
    },
    "query": "query PropertyFilteredReviewsQuery($context: ContextInput!, $propertyId: String!, $searchCriteria: PropertySearchCriteriaInput!) {\n  propertyReviewSummaries(\n    context: $context\n    propertyIds: [$propertyId]\n    searchCriteria: $searchCriteria\n  ) {\n    ...__PropertyReviewSummaryFragment\n    __typename\n  }\n  propertyInfo(context: $context, propertyId: $propertyId) {\n    id\n    reviewInfo(searchCriteria: $searchCriteria) {\n      ...__PropertyReviewsListFragment\n      sortAndFilter {\n        ...TravelerTypeFragment\n        ...SortTypeFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment __PropertyReviewSummaryFragment on PropertyReviewSummary {\n  accessibilityLabel\n  overallScoreWithDescription\n  propertyReviewCountDetails {\n    fullDescription\n    __typename\n  }\n  ...ReviewDisclaimerFragment\n  reviewSummaryDetails {\n    label\n    ratingPercentage\n    formattedRatingOutOfMax\n    __typename\n  }\n  totalCount {\n    raw\n    __typename\n  }\n  __typename\n}\n\nfragment ReviewDisclaimerFragment on PropertyReviewSummary {\n  reviewDisclaimer\n  reviewDisclaimerLabel\n  reviewDisclaimerAnalytics {\n    referrerId\n    linkName\n    __typename\n  }\n  reviewDisclaimerUrl {\n    value\n    accessibilityLabel\n    link {\n      url\n      __typename\n    }\n    __typename\n  }\n  reviewDisclaimerAccessibilityLabel\n  __typename\n}\n\nfragment __PropertyReviewsListFragment on PropertyReviews {\n  summary {\n    paginateAction {\n      text\n      analytics {\n        referrerId\n        linkName\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  reviews {\n    contentDirectFeedbackPromptId\n    ...ReviewParentFragment\n    managementResponses {\n      ...ReviewChildFragment\n      __typename\n    }\n    reviewInteractionSections {\n      primaryDisplayString\n      reviewInteractionType\n      __typename\n    }\n    __typename\n  }\n  ...NoResultsMessageFragment\n  __typename\n}\n\nfragment ReviewParentFragment on PropertyReview {\n  id\n  superlative\n  locale\n  title\n  brandType\n  reviewScoreWithDescription {\n    label\n    value\n    __typename\n  }\n  text\n  seeMoreAnalytics {\n    linkName\n    referrerId\n    __typename\n  }\n  submissionTime {\n    longDateFormat\n    __typename\n  }\n  impressionAnalytics {\n    event\n    referrerId\n    __typename\n  }\n  themes {\n    ...ReviewThemeFragment\n    __typename\n  }\n  reviewFooter {\n    ...PropertyReviewFooterSectionFragment\n    __typename\n  }\n  ...FeedbackIndicatorFragment\n  ...AuthorFragment\n  ...PhotosFragment\n  ...TravelersFragment\n  ...ReviewTranslationInfoFragment\n  ...PropertyReviewSourceFragment\n  ...PropertyReviewRegionFragment\n  __typename\n}\n\nfragment AuthorFragment on PropertyReview {\n  reviewAuthorAttribution {\n    text\n    __typename\n  }\n  __typename\n}\n\nfragment PhotosFragment on PropertyReview {\n  id\n  photoSection {\n    imageClickAnalytics {\n      referrerId\n      linkName\n      __typename\n    }\n    exitAnalytics {\n      referrerId\n      linkName\n      __typename\n    }\n    navClickAnalytics {\n      referrerId\n      linkName\n      __typename\n    }\n    __typename\n  }\n  photos {\n    description\n    url\n    __typename\n  }\n  __typename\n}\n\nfragment TravelersFragment on PropertyReview {\n  travelers\n  __typename\n}\n\nfragment ReviewThemeFragment on ReviewThemes {\n  icon {\n    id\n    __typename\n  }\n  label\n  __typename\n}\n\nfragment FeedbackIndicatorFragment on PropertyReview {\n  reviewInteractionSections {\n    primaryDisplayString\n    accessibilityLabel\n    reviewInteractionType\n    feedbackAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReviewTranslationInfoFragment on PropertyReview {\n  translationInfo {\n    loadingTranslationText\n    targetLocale\n    translatedBy {\n      description\n      __typename\n    }\n    translationCallToActionLabel\n    seeOriginalText\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyReviewSourceFragment on PropertyReview {\n  propertyReviewSource {\n    accessibilityLabel\n    graphic {\n      description\n      id\n      size\n      token\n      url {\n        value\n        __typename\n      }\n      __typename\n    }\n    text {\n      value\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyReviewRegionFragment on PropertyReview {\n  reviewRegion {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyReviewFooterSectionFragment on PropertyReviewFooterSection {\n  messages {\n    seoStructuredData {\n      itemscope\n      itemprop\n      itemtype\n      content\n      __typename\n    }\n    text {\n      ... on EGDSPlainText {\n        text\n        __typename\n      }\n      ... on EGDSGraphicText {\n        text\n        graphic {\n          ... on Mark {\n            description\n            id\n            size\n            url {\n              ... on HttpURI {\n                relativePath\n                value\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ReviewChildFragment on ManagementResponse {\n  id\n  header {\n    text\n    __typename\n  }\n  response\n  __typename\n}\n\nfragment NoResultsMessageFragment on PropertyReviews {\n  noResultsMessage {\n    __typename\n    ...MessagingCardFragment\n    ...EmptyStateFragment\n  }\n  __typename\n}\n\nfragment MessagingCardFragment on UIMessagingCard {\n  graphic {\n    __typename\n    ... on Icon {\n      id\n      description\n      __typename\n    }\n  }\n  primary\n  secondaries\n  __typename\n}\n\nfragment EmptyStateFragment on UIEmptyState {\n  heading\n  body\n  __typename\n}\n\nfragment TravelerTypeFragment on SortAndFilterViewModel {\n  sortAndFilter {\n    name\n    label\n    options {\n      label\n      isSelected\n      optionValue\n      description\n      clickAnalytics {\n        linkName\n        referrerId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SortTypeFragment on SortAndFilterViewModel {\n  sortAndFilter {\n    name\n    label\n    clickAnalytics {\n      linkName\n      referrerId\n      __typename\n    }\n    options {\n      label\n      isSelected\n      optionValue\n      description\n      clickAnalytics {\n        linkName\n        referrerId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
  }
])