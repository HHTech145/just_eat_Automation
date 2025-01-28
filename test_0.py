from bs4 import BeautifulSoup



html_content="""

<div data-v-6ad0c37a="" class="flex flex-col relative order-3 md:order-1 w-full md:w-8/12 lg:w-9/12"><div class="space-y-6"><div class="flex flex-col pb-6 border-b border-grey-30 last:border-b-0"><span class="order-date mb-4 text-xl font-bold inline-flex items-end flex-none w-full"><span class="text-sm lg:text-base font-normal uppercase leading-none"> Sat </span><span data-cy="orderDate" class="leading-none ml-2"> 16 Nov </span></span><div class="flex flex-col flex-1 space-y-4"><div data-v-1b554963="" class="card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed"><span data-v-1b554963="" data-cy="orderTime" class="w-1/2 xl:w-1/12 order-1 mb-6 xl:mb-0"> 15:32 </span><span data-v-1b554963="" tabindex="0" data-cy="orderId" class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> #441965622 </span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 lg:w-3/12 xl:w-2/12 order-5 lg:order-3 mb-0"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 order-6 lg:order-4 lg:w-2/12 xl:w-2/12"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M15.556 5.884l1.11-1.016v11.035c0 1.342-1.088 2.43-2.43 2.43H5.764c-1.342 0-2.43-1.088-2.43-2.43V4.868l1.11 1.016 1.112-1.016 1.11 1.016.348-.319v-1.94c0-1.311 1.063-2.374 2.373-2.375h1.226c1.31.001 2.373 1.064 2.373 2.375v1.94l.347.319 1.111-1.016 1.112 1.016zM7.5 10l-.833 3.333H12.5L13.333 10H7.5zm1.887-7.222c-.225 0-.44.088-.6.247-.16.159-.25.375-.25.6v1.944l.347.315L10 4.868l1.111 1.016.347-.315V3.625c0-.467-.378-.846-.845-.847H9.387z" transform="translate(-615 -398) translate(211 372) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Collection </span></span><span data-v-1b554963="" class="flex w-1/2 xl:w-1/12 justify-end order-2 xl:order-5 mb-6 xl:mb-0 relative"><span data-v-1b554963="" data-cy="orderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><hr data-v-1b554963="" class="line block xl:hidden border-grey-20 absolute left-0 transform -translate-x-1/2"></span><span data-v-1b554963="" data-cy="deliveryPrice" class="w-full sm:w-1/3 mt-4 sm:mt-0 whitespace-no-wrap lg:w-3/12 xl:w-3/12 font-bold sm:text-right lg:text-left xl:text-right order-7 lg:order-6"> £0.00 <span data-v-1b554963="" class="sm:text-xs">delivery fees</span></span><span data-v-1b554963="" data-cy="orderPrice" class="w-1/2 lg:w-1/12 xl:w-1/12 font-bold text-right order-4 lg:order-7 mb-6 lg:mb-0"> £2.29 </span></div></div></div><div class="flex flex-col pb-6 border-b border-grey-30 last:border-b-0"><span class="order-date mb-4 text-xl font-bold inline-flex items-end flex-none w-full"><span class="text-sm lg:text-base font-normal uppercase leading-none"> Wed </span><span data-cy="orderDate" class="leading-none ml-2"> 13 Nov </span></span><div class="flex flex-col flex-1 space-y-4"><div data-v-1b554963="" class="card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed"><span data-v-1b554963="" data-cy="orderTime" class="w-1/2 xl:w-1/12 order-1 mb-6 xl:mb-0"> 20:18 </span><span data-v-1b554963="" tabindex="0" data-cy="orderId" class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> #439876351 </span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 lg:w-3/12 xl:w-2/12 order-5 lg:order-3 mb-0"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 order-6 lg:order-4 lg:w-2/12 xl:w-2/12"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M14.664 10.093c1.823.97 2.836 2.677 2.836 4.918v.834c0 .919-.748 1.667-1.667 1.667H14.43c-.543.328-1.804.833-4.43.833-2.031 0-3.121-.505-3.615-.833H5c-.919 0-1.667-.748-1.667-1.667v-.834c0-2.228 1.006-3.93 2.816-4.904 1.087 1.421 2.76 2.393 4.2 2.393h.135c1.42 0 3.087-.993 4.18-2.407zm-4.18-8.427c2.49 0 4.517 1.889 4.517 4.21V6.98c0 2.37-2.586 4.685-4.516 4.685h-.135c-1.972 0-4.515-2.271-4.515-4.685V5.876c0-2.321 2.024-4.21 4.515-4.21zM12.9 5H7.934c-.24 0-.434.195-.434.434V7.08c0 .09.028.178.08.25 1.01 1.425 2.54 1.497 2.837 1.497 1.692 0 2.66-1.246 2.836-1.496.053-.073.08-.161.08-.251V5.434c0-.24-.194-.434-.434-.434z" transform="translate(-615 -310) translate(211 284) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Delivery </span></span><span data-v-1b554963="" class="flex w-1/2 xl:w-1/12 justify-end order-2 xl:order-5 mb-6 xl:mb-0 relative"><span data-v-1b554963="" data-cy="orderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><hr data-v-1b554963="" class="line block xl:hidden border-grey-20 absolute left-0 transform -translate-x-1/2"></span><span data-v-1b554963="" data-cy="deliveryPrice" class="w-full sm:w-1/3 mt-4 sm:mt-0 whitespace-no-wrap lg:w-3/12 xl:w-3/12 font-bold sm:text-right lg:text-left xl:text-right order-7 lg:order-6"> £0.49 <span data-v-1b554963="" class="sm:text-xs">delivery fees</span></span><span data-v-1b554963="" data-cy="orderPrice" class="w-1/2 lg:w-1/12 xl:w-1/12 font-bold text-right order-4 lg:order-7 mb-6 lg:mb-0"> £22.11 </span></div></div></div><div class="flex flex-col pb-6 border-b border-grey-30 last:border-b-0"><span class="order-date mb-4 text-xl font-bold inline-flex items-end flex-none w-full"><span class="text-sm lg:text-base font-normal uppercase leading-none"> Mon </span><span data-cy="orderDate" class="leading-none ml-2"> 11 Nov </span></span><div class="flex flex-col flex-1 space-y-4"><div data-v-1b554963="" class="card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed"><span data-v-1b554963="" data-cy="orderTime" class="w-1/2 xl:w-1/12 order-1 mb-6 xl:mb-0"> 18:49 </span><span data-v-1b554963="" tabindex="0" data-cy="orderId" class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> #438473194 </span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 lg:w-3/12 xl:w-2/12 order-5 lg:order-3 mb-0"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 order-6 lg:order-4 lg:w-2/12 xl:w-2/12"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M14.664 10.093c1.823.97 2.836 2.677 2.836 4.918v.834c0 .919-.748 1.667-1.667 1.667H14.43c-.543.328-1.804.833-4.43.833-2.031 0-3.121-.505-3.615-.833H5c-.919 0-1.667-.748-1.667-1.667v-.834c0-2.228 1.006-3.93 2.816-4.904 1.087 1.421 2.76 2.393 4.2 2.393h.135c1.42 0 3.087-.993 4.18-2.407zm-4.18-8.427c2.49 0 4.517 1.889 4.517 4.21V6.98c0 2.37-2.586 4.685-4.516 4.685h-.135c-1.972 0-4.515-2.271-4.515-4.685V5.876c0-2.321 2.024-4.21 4.515-4.21zM12.9 5H7.934c-.24 0-.434.195-.434.434V7.08c0 .09.028.178.08.25 1.01 1.425 2.54 1.497 2.837 1.497 1.692 0 2.66-1.246 2.836-1.496.053-.073.08-.161.08-.251V5.434c0-.24-.194-.434-.434-.434z" transform="translate(-615 -310) translate(211 284) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Delivery </span></span><span data-v-1b554963="" class="flex w-1/2 xl:w-1/12 justify-end order-2 xl:order-5 mb-6 xl:mb-0 relative"><span data-v-1b554963="" data-cy="orderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><hr data-v-1b554963="" class="line block xl:hidden border-grey-20 absolute left-0 transform -translate-x-1/2"></span><span data-v-1b554963="" data-cy="deliveryPrice" class="w-full sm:w-1/3 mt-4 sm:mt-0 whitespace-no-wrap lg:w-3/12 xl:w-3/12 font-bold sm:text-right lg:text-left xl:text-right order-7 lg:order-6"> £0.49 <span data-v-1b554963="" class="sm:text-xs">delivery fees</span></span><span data-v-1b554963="" data-cy="orderPrice" class="w-1/2 lg:w-1/12 xl:w-1/12 font-bold text-right order-4 lg:order-7 mb-6 lg:mb-0"> £23.77 </span></div><div data-v-1b554963="" class="card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed"><span data-v-1b554963="" data-cy="orderTime" class="w-1/2 xl:w-1/12 order-1 mb-6 xl:mb-0"> 18:22 </span><span data-v-1b554963="" tabindex="0" data-cy="orderId" class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> #438440764 </span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 lg:w-3/12 xl:w-2/12 order-5 lg:order-3 mb-0"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 order-6 lg:order-4 lg:w-2/12 xl:w-2/12"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M14.664 10.093c1.823.97 2.836 2.677 2.836 4.918v.834c0 .919-.748 1.667-1.667 1.667H14.43c-.543.328-1.804.833-4.43.833-2.031 0-3.121-.505-3.615-.833H5c-.919 0-1.667-.748-1.667-1.667v-.834c0-2.228 1.006-3.93 2.816-4.904 1.087 1.421 2.76 2.393 4.2 2.393h.135c1.42 0 3.087-.993 4.18-2.407zm-4.18-8.427c2.49 0 4.517 1.889 4.517 4.21V6.98c0 2.37-2.586 4.685-4.516 4.685h-.135c-1.972 0-4.515-2.271-4.515-4.685V5.876c0-2.321 2.024-4.21 4.515-4.21zM12.9 5H7.934c-.24 0-.434.195-.434.434V7.08c0 .09.028.178.08.25 1.01 1.425 2.54 1.497 2.837 1.497 1.692 0 2.66-1.246 2.836-1.496.053-.073.08-.161.08-.251V5.434c0-.24-.194-.434-.434-.434z" transform="translate(-615 -310) translate(211 284) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Delivery </span></span><span data-v-1b554963="" class="flex w-1/2 xl:w-1/12 justify-end order-2 xl:order-5 mb-6 xl:mb-0 relative"><span data-v-1b554963="" data-cy="orderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><hr data-v-1b554963="" class="line block xl:hidden border-grey-20 absolute left-0 transform -translate-x-1/2"></span><span data-v-1b554963="" data-cy="deliveryPrice" class="w-full sm:w-1/3 mt-4 sm:mt-0 whitespace-no-wrap lg:w-3/12 xl:w-3/12 font-bold sm:text-right lg:text-left xl:text-right order-7 lg:order-6"> £0.49 <span data-v-1b554963="" class="sm:text-xs">delivery fees</span></span><span data-v-1b554963="" data-cy="orderPrice" class="w-1/2 lg:w-1/12 xl:w-1/12 font-bold text-right order-4 lg:order-7 mb-6 lg:mb-0"> £25.10 </span></div></div></div><div class="flex flex-col pb-6 border-b border-grey-30 last:border-b-0"><span class="order-date mb-4 text-xl font-bold inline-flex items-end flex-none w-full"><span class="text-sm lg:text-base font-normal uppercase leading-none"> Wed </span><span data-cy="orderDate" class="leading-none ml-2"> 6 Nov </span></span><div class="flex flex-col flex-1 space-y-4"><div data-v-1b554963="" class="card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed"><span data-v-1b554963="" data-cy="orderTime" class="w-1/2 xl:w-1/12 order-1 mb-6 xl:mb-0"> 21:47 </span><span data-v-1b554963="" tabindex="0" data-cy="orderId" class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> #434376512 </span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 lg:w-3/12 xl:w-2/12 order-5 lg:order-3 mb-0"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span><span data-v-1b554963="" class="inline-flex items-center w-1/2 sm:w-1/3 order-6 lg:order-4 lg:w-2/12 xl:w-2/12"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M14.664 10.093c1.823.97 2.836 2.677 2.836 4.918v.834c0 .919-.748 1.667-1.667 1.667H14.43c-.543.328-1.804.833-4.43.833-2.031 0-3.121-.505-3.615-.833H5c-.919 0-1.667-.748-1.667-1.667v-.834c0-2.228 1.006-3.93 2.816-4.904 1.087 1.421 2.76 2.393 4.2 2.393h.135c1.42 0 3.087-.993 4.18-2.407zm-4.18-8.427c2.49 0 4.517 1.889 4.517 4.21V6.98c0 2.37-2.586 4.685-4.516 4.685h-.135c-1.972 0-4.515-2.271-4.515-4.685V5.876c0-2.321 2.024-4.21 4.515-4.21zM12.9 5H7.934c-.24 0-.434.195-.434.434V7.08c0 .09.028.178.08.25 1.01 1.425 2.54 1.497 2.837 1.497 1.692 0 2.66-1.246 2.836-1.496.053-.073.08-.161.08-.251V5.434c0-.24-.194-.434-.434-.434z" transform="translate(-615 -310) translate(211 284) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Delivery </span></span><span data-v-1b554963="" class="flex w-1/2 xl:w-1/12 justify-end order-2 xl:order-5 mb-6 xl:mb-0 relative"><span data-v-1b554963="" data-cy="orderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><hr data-v-1b554963="" class="line block xl:hidden border-grey-20 absolute left-0 transform -translate-x-1/2"></span><span data-v-1b554963="" data-cy="deliveryPrice" class="w-full sm:w-1/3 mt-4 sm:mt-0 whitespace-no-wrap lg:w-3/12 xl:w-3/12 font-bold sm:text-right lg:text-left xl:text-right order-7 lg:order-6"> £2.99 <span data-v-1b554963="" class="sm:text-xs">delivery fees</span></span><span data-v-1b554963="" data-cy="orderPrice" class="w-1/2 lg:w-1/12 xl:w-1/12 font-bold text-right order-4 lg:order-7 mb-6 lg:mb-0"> £13.97 </span></div></div></div></div><div></div><div data-v-197b108c="" data-theme="icing" class="pc-back-to-top"><button data-v-197b108c="" class="pc-back-to-top-button md:ml-6 flex left-full"><svg data-v-197b108c="" width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" class="fill-current pc-back-to-top-icon"><path d="M8.65625 14.125V3.93126L11.9463 7.22126L12.8738 6.29376L8.77 2.19876C8.66915 2.09717 8.54919 2.01654 8.41704 1.96152C8.28488 1.9065 8.14315 1.87817 8 1.87817C7.85685 1.87817 7.71512 1.9065 7.58296 1.96152C7.45081 2.01654 7.33085 2.09717 7.23 2.19876L3.12625 6.29376L4.05375 7.22126L7.34375 3.93126V14.125H8.65625Z"></path></svg> <span data-v-197b108c="" class="pc-back-to-top-text max-w-0">
      Back to the top
    </span></button></div></div>

"""


# # Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# # Extract data
# orders = []
# order_divs = soup.find_all("div", class_="flex flex-col pb-6 border-b border-grey-30 last:border-b-0")

# for order_div in order_divs:
#     order = {}
#     order['date'] = order_div.find("span", {"data-cy": "orderDate"}).get_text(strip=True)
#     order['time'] = order_div.find("span", {"data-cy": "orderTime"}).get_text(strip=True)
#     order['order_id'] = order_div.find("span", {"data-cy": "orderId"}).get_text(strip=True)
#     order['payment_type'] = order_div.find("span", {"data-cy": "orderPaymentType"}).get_text(strip=True)
#     order['service_type'] = order_div.find("span", {"data-cy": "orderServiceType"}).get_text(strip=True)
#     order['delivery_price'] = order_div.find("span", {"data-cy": "deliveryPrice"}).get_text(strip=True)
#     order['order_price'] = order_div.find("span", {"data-cy": "orderPrice"}).get_text(strip=True)
#     orders.append(order)


    

# # Print the extracted orders
# for idx, order in enumerate(orders, start=1):
#     print(f"Order {idx}:")
#     for key, value in order.items():
#         print(f"  {key.capitalize()}: {value}")
#     print()



###########################################################################################################################
# orders = []
# order_divs = soup.find_all("div", class_="flex flex-col pb-6 border-b border-grey-30 last:border-b-0")

# for order_div in order_divs:

#     # Find all order cards
#     order_cards = order_div.find_all('div', class_='card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed')

#     # Extract data for each order
#     # orders = []
#     print("length of divs",len(order_cards))
#     for card in order_cards:
#         time = card.find('span', {'data-cy': 'orderTime'}).get_text(strip=True)
#         order_id = card.find('span', {'data-cy': 'orderId'}).get_text(strip=True)
#         payment_type = card.find('span', {'data-cy': 'orderPaymentType'}).get_text(strip=True)
#         service_type = card.find('span', {'data-cy': 'orderServiceType'}).get_text(strip=True)
#         status = card.find('span', {'data-cy': 'orderStatus'}).get_text(strip=True)
#         delivery_price = card.find('span', {'data-cy': 'deliveryPrice'}).get_text(strip=True)
#         order_price = card.find('span', {'data-cy': 'orderPrice'}).get_text(strip=True)
        
#         # Append extracted data as a dictionary
#         orders.append({
#             'time': time,
#             'order_id': order_id,
#             'payment_type': payment_type,
#             'service_type': service_type,
#             'status': status,
#             'delivery_price': delivery_price,
#             'order_price': order_price,
#         })

# # Print the extracted data
# for order in orders:
#     print(order)

########################################################################################################################################
# print("##############################################################################################################")
# from datetime import datetime

# orders = []
# order_divs = soup.find_all("div", class_="flex flex-col pb-6 border-b border-grey-30 last:border-b-0")

# for order_div in order_divs:

#     # Extract the order date
#     order_date_text = order_div.find('span', {'data-cy': 'orderDate'}).get_text(strip=True)
#     order_date = datetime.strptime(order_date_text + " 2024", "%d %b %Y")  # Add the year

#     # Find all order cards
#     order_cards = order_div.find_all('div', class_='card bg-white rounded-sm border border-grey-30 p-4 md:p-6 flex items-center relative flex-wrap completed')

#     # Extract data for each order
#     for card in order_cards:
#         time = card.find('span', {'data-cy': 'orderTime'}).get_text(strip=True)
#         order_id = card.find('span', {'data-cy': 'orderId'}).get_text(strip=True)
#         payment_type = card.find('span', {'data-cy': 'orderPaymentType'}).get_text(strip=True)
#         service_type = card.find('span', {'data-cy': 'orderServiceType'}).get_text(strip=True)
#         status = card.find('span', {'data-cy': 'orderStatus'}).get_text(strip=True)
#         delivery_price = card.find('span', {'data-cy': 'deliveryPrice'}).get_text(strip=True)
#         order_price = card.find('span', {'data-cy': 'orderPrice'}).get_text(strip=True)
        

#         # Locate the clickable order_id element using Selenium
#         clickable_element = driver.find_element(By.XPATH, f"//span[@data-cy='orderId' and text()='{order_id}']")
#         # Append extracted data as a dictionary
#         orders.append({
#             'date': order_date,  # Include the parsed date
#             'time': time,
#             'order_id': order_id,
#             'payment_type': payment_type,
#             'service_type': service_type,
#             'status': status,
#             'delivery_price': delivery_price,
#             'order_price': order_price,
#             'clickable_element': clickable_element,  # Add the clickable element
#         })



# # Sort the orders by date
# orders = sorted(orders, key=lambda x: x['date'])

# # Print the sorted orders
# for order in orders:
#     print(order)


#########################################################################################################

# <span data-v-1b554963="" tabindex="0" 
# data-cy="orderId" 
# class="font-bold w-1/2 lg:w-3/12 xl:w-2/12 text-blue-100 hover:underline order-3 xl:order-2 mb-6 lg:mb-0 text-left xl:text-center cursor-pointer"> 
# #441965622 </span>



########################## order details ####################################################################################

from bs4 import BeautifulSoup

# Assuming `html_content` contains the HTML content you provided
html_content = '''

<div class="p-4 md:p-6 bg-white rounded-sm shadow-md"><div class="flex justify-between flex-col md:flex-row space-y-6 md:space-y-0"><div class="flex flex-col md:flex-row md:space-x-3 -mx-4 px-4 pt-4 pb-2 -mb-2 -mt-4 md:p-0 md:m-0"><img src="http://d30v2pzvrfyzpo.cloudfront.net/uk/images/restaurants/137207.gif" alt="" width="34" height="34" class="rounded w-12 h-12"><div class="flex flex-col space-y-1"><span data-cy="orderDetailsRestaurantName" class="font-bold"> Maeme's Piri Piri Southall </span><span data-cy="orderDetailsRestaurantAddress"> 10 High Street, UB1 3DA </span></div></div><div class="flex flex-col items-start md:items-end space-y-2"><span data-cy="orderDetailsOrderStatus" class="inline-flex text-xs px-2 box-border bg-green-10"> Completed </span><span class="text-xl"><span>Order #</span><span data-cy="orderDetailsOrderId" class="font-bold"> 438473194 </span></span><p data-cy="orderPlacedDate" class="md:space-x-4 flex flex-col lg:flex-row space-y-2 md:space-y-0"><span>Order placed: 18:49 on 11 Nov 2024</span><span>Order due: ASAP on 11 Nov 2024</span></p></div></div><div class="flex justify-between items-start md:items-center flex-col md:flex-row space-y-4 md:space-y-0 mt-4 md:mt-0"><div class="flex md:space-x-6 space-y-4 md:space-y-0 flex-col md:flex-row"><span class="inline-flex items-center"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" class="flex-shrink-0"><g fill="none" fill-rule="evenodd"><g><g><g><g><path fill="#5E6B77" d="M14.664 10.093c1.823.97 2.836 2.677 2.836 4.918v.834c0 .919-.748 1.667-1.667 1.667H14.43c-.543.328-1.804.833-4.43.833-2.031 0-3.121-.505-3.615-.833H5c-.919 0-1.667-.748-1.667-1.667v-.834c0-2.228 1.006-3.93 2.816-4.904 1.087 1.421 2.76 2.393 4.2 2.393h.135c1.42 0 3.087-.993 4.18-2.407zm-4.18-8.427c2.49 0 4.517 1.889 4.517 4.21V6.98c0 2.37-2.586 4.685-4.516 4.685h-.135c-1.972 0-4.515-2.271-4.515-4.685V5.876c0-2.321 2.024-4.21 4.515-4.21zM12.9 5H7.934c-.24 0-.434.195-.434.434V7.08c0 .09.028.178.08.25 1.01 1.425 2.54 1.497 2.837 1.497 1.692 0 2.66-1.246 2.836-1.496.053-.073.08-.161.08-.251V5.434c0-.24-.194-.434-.434-.434z" transform="translate(-615 -310) translate(211 284) translate(404 24) translate(0 2)"></path></g></g></g></g></g></svg><span data-cy="orderServiceType" class="ml-2"> Delivery </span></span><span class="inline-flex items-center"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" viewBox="0 0 20 20"><defs><path id="qnxpmlkpra" d="M18.333 6.667H1.667v-.741c0-1.432 1.088-2.593 2.43-2.593h11.806c1.342 0 2.43 1.161 2.43 2.593v.74zm0 2.5v5c0 1.38-1.088 2.5-2.43 2.5H4.097c-1.342 0-2.43-1.12-2.43-2.5v-5h16.666z"></path></defs><g fill="none" fill-rule="evenodd"><g><g><g><g transform="translate(-483 -310) translate(211 284) translate(272 24) translate(0 2)"><use fill="#5E6B77" xlink:href="#qnxpmlkpra"></use></g></g></g></g></g></svg><span data-cy="orderPaymentType" class="ml-2"> Card </span></span></div><span data-cy="orderTransactionNumber"> Transaction no. PBC733FDH6TMLNF3 </span></div><hr class="my-5 border-grey-30 -mx-4 sm:hidden"><div class="hidden md:flex mt-5 bg-grey-20 p-4"><span class="w-1/2 md:w-1/12 order-1 mb-6 lg:mb-0"> Pcs. </span><span class="w-1/2 md:w-3/12 order-3 md:order-2 mb-6 lg:mb-0"> Name </span><span class="w-1/2 md:w-4/12 order-5 md:order-3 md:mb-6 lg:mb-0 md:justify-end lg:justify-start"> Description </span><span class="flex w-1/2 md:w-2/12 justify-end md:justify-center lg:justify-end order-2 md:order-5 mb-6 md:mb-0 relative"> Unit Price </span><span class="w-1/2 md:w-2/12 text-right order-4 md:order-6 mb-6 md:mb-0"> Total </span></div><div class="mt-5 md:px-4 mb-6"><span class="flex flex-wrap w-full"><span data-cy="orderDetailsItemQuantity" class="w-1/6 md:w-1/12 order-1 mb-2 md:mb-0 font-bold md:font-normal"> 1 x </span><span data-cy="orderDetailsItemName" class="w-3/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0"> Maeme's King <!----></span><span data-cy="orderDetailsItemDescription" class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start"> Flame grilled chicken breast marinated with our famous piri piri Flavours in a soft floured bap. </span><span data-cy="orderDetailsItemPrice" class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><span class="md:hidden mr-2">Unit Price &nbsp;</span><span>£9.99</span></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> £9.99 </span></span><span class="flex flex-col"><span><span class="flex flex-wrap w-full mt-4 justify-end"><span class="w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline"> Mango &amp; Lime <!----></span><span class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start">  </span><span class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><!----><!----></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> Free </span></span><!----></span><span><span class="flex flex-wrap w-full mt-4 justify-end"><span class="w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline"> Garlic Mayo <!----></span><span class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start">  </span><span class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><span class="md:hidden mr-2"> Unit Price &nbsp; </span><span> £0.50 </span></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> £0.50 </span></span><!----></span></span><hr class="my-5 border-grey-30 md:hidden"></div><div class="mt-5 md:px-4 mb-6"><span class="flex flex-wrap w-full"><span data-cy="orderDetailsItemQuantity" class="w-1/6 md:w-1/12 order-1 mb-2 md:mb-0 font-bold md:font-normal"> 1 x </span><span data-cy="orderDetailsItemName" class="w-3/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0"> 5 x Tender Strips <!----></span><span data-cy="orderDetailsItemDescription" class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start"> 5 x Succulent Strips of piri piri chicken. </span><span data-cy="orderDetailsItemPrice" class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><span class="md:hidden mr-2">Unit Price &nbsp;</span><span>£9.99</span></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> £9.99 </span></span><span class="flex flex-col"><span><span class="flex flex-wrap w-full mt-4 justify-end"><span class="w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline"> Lemon &amp; Herb <!----></span><span class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start">  </span><span class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><!----><!----></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> Free </span></span><!----></span><span><span class="flex flex-wrap w-full mt-4 justify-end"><span class="w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline"> Piri Piri Mayo <!----></span><span class="w-full md:w-4/12 order-4 md:order-3 mb-2 md:mb-0 md:justify-end lg:justify-start">  </span><span class="flex w-full md:w-2/12 justify-start md:justify-center lg:justify-end order-5 md:order-5 relative text-grey-50 md:text-grey-100"><span class="md:hidden mr-2"> Unit Price &nbsp; </span><span> £0.50 </span></span><span data-cy="orderDetailsItemTotalPrice" class="w-2/6 md:w-2/12 text-right order-3 md:order-6 mb-2 md:mb-0 font-bold md:font-normal"> £0.50 </span></span><!----></span></span><hr class="my-5 border-grey-30 md:hidden hidden"></div><!----><!----><hr class="my-5 border-grey-30 -mx-4 sm:mx-0"><div class="flex flex-col sm:px-4 space-y-5"><span class="inline-flex justify-end"><span class="flex w-1/2 md:w-4/12 justify-start md:justify-center lg:justify-end order-2 md:order-5 mb-6 md:mb-0 relative"> Service charges </span><span data-cy="orderDetailsserviceFee" class="w-1/2 md:w-2/12 text-right order-4 md:order-6 mb-6 md:mb-0"> £2.30 </span></span><!----><span class="inline-flex justify-end"><span data-cy="orderDetailsDeliveryFee" class="flex w-1/2 md:w-4/12 justify-start md:justify-center lg:justify-end order-2 md:order-5 mb-6 md:mb-0 relative"> Delivery fees </span><span class="w-1/2 md:w-2/12 text-right order-4 md:order-6 mb-6 md:mb-0"> £0.49 </span></span><!----><!----><!----><!----><!----><span class="inline-flex justify-end text-xl font-bold"><span class="flex w-1/2 md:w-4/12 justify-start md:justify-center lg:justify-end order-2 md:order-5 mb-6 md:mb-0"> Total </span><span data-cy="orderDetailsTotal" class="w-1/2 md:w-2/12 text-right order-4 md:order-6 mb-6 md:mb-0"> £23.77 </span></span></div></div>


'''

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting restaurant information
# restaurant_name = soup.find('span', {'data-cy': 'orderDetailsRestaurantName'}).text.strip()
# restaurant_address = soup.find('span', {'data-cy': 'orderDetailsRestaurantAddress'}).text.strip()

# # Extracting order details
# order_id = soup.find('span', {'data-cy': 'orderDetailsOrderId'}).text.strip()
# order_status = soup.find('span', {'data-cy': 'orderDetailsOrderStatus'}).text.strip()
# order_placed_date = soup.find('span', {'data-cy': 'orderPlacedDate'}).text.strip()

# # Extracting order items
# order_items = []
# items = soup.find_all('span', {'data-cy': 'orderDetailsItemName'})
# print(items,len(items))
# # for item in items:
# #     item_name = item.text.strip()
# #     item_quantity = item.find_previous('span', {'data-cy': 'orderDetailsItemQuantity'}).text.strip()
# #     item_description = item.find_next('span', {'data-cy': 'orderDetailsItemDescription'}).text.strip()
# #     item_price = item.find_next('span', {'data-cy': 'orderDetailsItemPrice'}).text.strip()
# #     item_total_price = item.find_next('span', {'data-cy': 'orderDetailsItemTotalPrice'}).text.strip()
    
# #     order_items.append({
# #         'name': item_name,
# #         'quantity': item_quantity,
# #         'description': item_description,
# #         'unit_price': item_price,
# #         'total_price': item_total_price
# #     })

# # # Extracting other details (e.g., service type, payment type)
# # service_type = soup.find('span', {'data-cy': 'orderServiceType'}).text.strip()
# # payment_type = soup.find('span', {'data-cy': 'orderPaymentType'}).text.strip()
# # transaction_number = soup.find('span', {'data-cy': 'orderTransactionNumber'}).text.strip()

# # Print extracted details
# print(f"Restaurant Name: {restaurant_name}")
# print(f"Restaurant Address: {restaurant_address}")
# print(f"Order ID: {order_id}")
# print(f"Order Status: {order_status}")
# print(f"Order Placed Date: {order_placed_date}")
# # print(f"Service Type: {service_type}")
# # print(f"Payment Type: {payment_type}")
# # print(f"Transaction Number: {transaction_number}")
# print("\nOrder Items:")
# for item in order_items:
#     print(f"{item['quantity']} {item['name']} - {item['description']}")
#     print(f"Unit Price: {item['unit_price']} - Total Price: {item['total_price']}")



###########################################################################################

# Extract restaurant details
# from bs4 import BeautifulSoup

# Assuming soup is already initialized with the page content

# Extract basic order details
restaurant_name = soup.find('span', {'data-cy': 'orderDetailsRestaurantName'}).text.strip()
restaurant_address = soup.find('span', {'data-cy': 'orderDetailsRestaurantAddress'}).text.strip()

order_id = soup.find('span', {'data-cy': 'orderDetailsOrderId'}).text.strip()
order_status = soup.find('span', {'data-cy': 'orderDetailsOrderStatus'}).text.strip()

# Extract order placed date
order_placed_element = soup.find('span', {'data-cy': 'orderPlacedDate'})

if order_placed_element:
    order_placed = order_placed_element.text.strip()
else:
    order_placed = 'N/A'  # or handle as appropriate

# Find all meal blocks
meal_blocks = soup.find_all('div', class_=lambda x: x and 'mt-5' in x and 'md:px-4' in x and 'mb-6' in x)
print(f"Number of meal blocks: {len(meal_blocks)}")

# Loop through each meal block to extract the items and their details
meal_details = []  # To store the extracted meal details

for meal in meal_blocks:
    # Extract individual items
    items = meal.find_all('span', {'data-cy': 'orderDetailsItemName'})
    quantities = meal.find_all('span', {'data-cy': 'orderDetailsItemQuantity'})
    unit_prices = meal.find_all('span', {'data-cy': 'orderDetailsItemPrice'})
    total_prices = meal.find_all('span', {'data-cy': 'orderDetailsItemTotalPrice'})
    
    # Ensure the lengths of all lists are the same (i.e., corresponding item details)
    num_items = len(items)
    for i in range(num_items):
        meal_detail = {
            'item_name': items[i].text.strip(),
            'quantity': quantities[i].text.strip(),
            'unit_price': unit_prices[i].text.strip(),
            'total_price': total_prices[i].text.strip(),
        }
        meal_details.append(meal_detail)

# Print the extracted data
print("Order Details:")
print(f"Restaurant: {restaurant_name}")
print(f"Address: {restaurant_address}")
print(f"Order ID: {order_id}")
print(f"Order Status: {order_status}")
print(f"Order Placed: {order_placed}")
print("\nMeal Details:")
for meal in meal_details:
    print(f"Item: {meal['item_name']}, Quantity: {meal['quantity']}, Unit Price: {meal['unit_price']}, Total Price: {meal['total_price']}")

# Optionally, store the data in a structured format (e.g., a CSV file, database, etc.)


#############################################################


from bs4 import BeautifulSoup

# Assuming soup is already initialized with the page content

# Extract basic order details
restaurant_name = soup.find('span', {'data-cy': 'orderDetailsRestaurantName'}).text.strip()
restaurant_address = soup.find('span', {'data-cy': 'orderDetailsRestaurantAddress'}).text.strip()

order_id = soup.find('span', {'data-cy': 'orderDetailsOrderId'}).text.strip()
order_status = soup.find('span', {'data-cy': 'orderDetailsOrderStatus'}).text.strip()

# Extract order placed date
order_placed_element = soup.find('span', {'data-cy': 'orderPlacedDate'})

if order_placed_element:
    order_placed = order_placed_element.text.strip()
else:
    order_placed = 'N/A'  # or handle as appropriate

# Find all meal blocks
meal_blocks = soup.find_all('div', class_=lambda x: x and 'mt-5' in x and 'md:px-4' in x and 'mb-6' in x)
print(f"Number of meal blocks: {len(meal_blocks)}")

# Loop through each meal block to extract the items and their details
meal_details = []  # To store the extracted meal details

for meal in meal_blocks:
    # Extract individual items
    items = meal.find_all('span', {'data-cy': 'orderDetailsItemName'})
    quantities = meal.find_all('span', {'data-cy': 'orderDetailsItemQuantity'})
    unit_prices = meal.find_all('span', {'data-cy': 'orderDetailsItemPrice'})
    total_prices = meal.find_all('span', {'data-cy': 'orderDetailsItemTotalPrice'})
    
    # Ensure the lengths of all lists are the same (i.e., corresponding item details)
    num_items = len(items)
    for i in range(num_items):
        meal_detail = {
            'item_name': items[i].text.strip(),
            'quantity': quantities[i].text.strip(),
            'unit_price': unit_prices[i].text.strip(),
            'total_price': total_prices[i].text.strip(),
        }
        meal_details.append(meal_detail)

    # Check for customization details within this meal block
    customization_blocks = meal.find_all('span', {'class': 'flex flex-wrap w-full mt-4 justify-end'})
    for customization in customization_blocks:
        customization_name = customization.find('span', {'class': 'w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline'})
        customization_price = customization.find('span', {'data-cy': 'orderDetailsItemTotalPrice'})
        
        if customization_name and customization_price:
            customization_detail = {
                'customization_name': customization_name.text.strip(),
                'customization_price': customization_price.text.strip(),
            }
            meal_details.append(customization_detail)

# Print the extracted data
print("Order Details:")
print(f"Restaurant: {restaurant_name}")
print(f"Address: {restaurant_address}")
print(f"Order ID: {order_id}")
print(f"Order Status: {order_status}")
print(f"Order Placed: {order_placed}")
print("\nMeal Details:")
for meal in meal_details:
    if 'item_name' in meal:
        print(f"Item: {meal['item_name']}, Quantity: {meal['quantity']}, Unit Price: {meal['unit_price']}, Total Price: {meal['total_price']}")
    elif 'customization_name' in meal:
        print(f"Customization: {meal['customization_name']}, Price: {meal['customization_price']}")


import re

def extract_meal_details(soup):
    order_meal_details = []

    # Find all meal blocks
    meal_blocks = soup.find_all('div', class_=lambda x: x and 'mt-5' in x and 'md:px-4' in x and 'mb-6' in x)

    for meal in meal_blocks:
        # Extract main meal details
        meal_name = meal.find('span', {'data-cy': 'orderDetailsItemName'}).text.strip()
        
        # Clean and parse meal price
        meal_price_text = meal.find('span', {'data-cy': 'orderDetailsItemPrice'}).text.strip()
        meal_price_text = meal_price_text.replace('\xa0', '')  # Remove non-breaking spaces
        meal_price_match = re.search(r"[\d\.]+", meal_price_text)  # Extract numeric value
        
        if meal_price_match:
            meal_price = float(meal_price_match.group())
        else:
            meal_price = 0.0  # Default price if extraction fails

        quantity = meal.find('span', {'data-cy': 'orderDetailsItemQuantity'}).text.strip()
        description_element = meal.find('span', {'data-cy': 'orderDetailsItemDescription'})
        description = description_element.text.strip() if description_element else "No description available"

        # Extract customizations
        customizations = []
        customization_blocks = meal.find_all('span', {'class': 'flex flex-wrap w-full mt-4 justify-end'})
        
        for customization in customization_blocks:
            customization_name_element = customization.find('span', {'class': 'w-4/6 md:w-3/12 order-2 md:order-2 mb-2 md:mb-0 underline'})
            customization_price_element = customization.find('span', {'data-cy': 'orderDetailsItemTotalPrice'})

            # Extract customization details if available
            customization_name = customization_name_element.text.strip() if customization_name_element else "Unknown"
            customization_price_text = customization_price_element.text.strip().replace('£', '') if customization_price_element else "Free"

            # Convert customization price to float
            customization_price = 0.0 if customization_price_text.lower() == "free" else float(customization_price_text)

            customizations.append({
                'customization': customization_name,
                'price': customization_price,
            })

        # Append the meal details
        order_meal_details.append({
            'meal_name': meal_name,
            'meal_price': meal_price,
            'quantity': quantity,
            'description': description,
            'customizations': customizations,
        })

    return {'order_meal_details': order_meal_details}

def extract_price_details(soup):
    # Extract order price details
    price_details = {}

    # Extract Service Charges
    service_fee_element = soup.find('span', {'data-cy': 'orderDetailsserviceFee'})
    if service_fee_element:
        price_details['service_fee'] = service_fee_element.text.strip()
    else:
        price_details['service_fee'] = 'N/A'

    # Extract Delivery Fee
    delivery_fee_element = soup.find('span', {'data-cy': 'orderDetailsDeliveryFee'})
    if delivery_fee_element:
        # Extract the text inside the parent span
        delivery_fee_text = delivery_fee_element.find_next('span').text.strip()
        price_details['delivery_fee'] = delivery_fee_text
    else:
        price_details['delivery_fee'] = 'N/A'

    # Extract Total Price
    total_price_element = soup.find('span', {'data-cy': 'orderDetailsTotal'})
    if total_price_element:
        price_details['total'] = total_price_element.text.strip()
    else:
        price_details['total'] = 'N/A'

    return price_details

# Assuming soup contains the page HTML
order_price_details = extract_price_details(soup)

# Now, print or use the extracted price details
print("Order Price Details:")
print(f"Service Fee: {order_price_details['service_fee']}")
print(f"Delivery Fee: {order_price_details['delivery_fee']}")
print(f"Total: {order_price_details['total']}")



# Assuming soup contains the HTML content
meal_details_dict = extract_meal_details(soup)


print(meal_details_dict)