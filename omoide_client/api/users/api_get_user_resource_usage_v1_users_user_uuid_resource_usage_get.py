from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_resource_usage_output import UserResourceUsageOutput
from ...types import Response


def _get_kwargs(
    user_uuid: UUID,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/users/{user_uuid}/resource_usage",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UserResourceUsageOutput]]:
    if response.status_code == 200:
        response_200 = UserResourceUsageOutput.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, UserResourceUsageOutput]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, UserResourceUsageOutput]]:
    """Api Get User Resource Usage

     Get resource usage info for specific user.

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserResourceUsageOutput]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, UserResourceUsageOutput]]:
    """Api Get User Resource Usage

     Get resource usage info for specific user.

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserResourceUsageOutput]
    """

    return sync_detailed(
        user_uuid=user_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, UserResourceUsageOutput]]:
    """Api Get User Resource Usage

     Get resource usage info for specific user.

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserResourceUsageOutput]]
    """

    kwargs = _get_kwargs(
        user_uuid=user_uuid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_uuid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, UserResourceUsageOutput]]:
    """Api Get User Resource Usage

     Get resource usage info for specific user.

    Args:
        user_uuid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserResourceUsageOutput]
    """

    return (
        await asyncio_detailed(
            user_uuid=user_uuid,
            client=client,
        )
    ).parsed
