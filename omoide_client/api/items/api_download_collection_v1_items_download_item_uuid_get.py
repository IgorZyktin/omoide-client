from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_uuid: UUID,
    *,
    response_class: Union[Unset, Any] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["response_class"] = response_class

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/items/download/{item_uuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    response_class: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Api Download Collection

     Return all children as a zip archive.

    WARNING - this endpoint works only behind NGINX with mod_zip installed.

    Args:
        item_uuid (UUID):
        response_class (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        item_uuid=item_uuid,
        response_class=response_class,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    response_class: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Api Download Collection

     Return all children as a zip archive.

    WARNING - this endpoint works only behind NGINX with mod_zip installed.

    Args:
        item_uuid (UUID):
        response_class (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        item_uuid=item_uuid,
        client=client,
        response_class=response_class,
    ).parsed


async def asyncio_detailed(
    item_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    response_class: Union[Unset, Any] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Api Download Collection

     Return all children as a zip archive.

    WARNING - this endpoint works only behind NGINX with mod_zip installed.

    Args:
        item_uuid (UUID):
        response_class (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        item_uuid=item_uuid,
        response_class=response_class,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    response_class: Union[Unset, Any] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Api Download Collection

     Return all children as a zip archive.

    WARNING - this endpoint works only behind NGINX with mod_zip installed.

    Args:
        item_uuid (UUID):
        response_class (Union[Unset, Any]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            item_uuid=item_uuid,
            client=client,
            response_class=response_class,
        )
    ).parsed