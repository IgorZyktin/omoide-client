from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_get_version_v1_info_version_get_response_api_get_version_v1_info_version_get import (
    ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet,
)
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/info/version",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    if response.status_code == 200:
        response_200 = ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    """Api Get Version

     Get current version of the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    """Api Get Version

     Get current version of the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    """Api Get Version

     Get current version of the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet]:
    """Api Get Version

     Get current version of the API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiGetVersionV1InfoVersionGetResponseApiGetVersionV1InfoVersionGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed