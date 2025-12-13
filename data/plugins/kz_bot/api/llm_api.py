from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.core.message.message_event_result import MessageChain
from astrbot.core.provider.entities import ProviderRequest


@register("llm", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.on_llm_request()
    async def my_custom_hook_1(self, event: AstrMessageEvent, req: ProviderRequest):  # 请注意有三个参数
        print(req)  # 打印请求的文本
        msg_chain = MessageChain()
        msg_chain.message("1233")
        await event.send(msg_chain)
        # async for ret in self.helloworld(event):
        #     if isinstance(ret, (MessageEventResult, CommandResult)):
        #         # 如果返回值是 MessageEventResult, 设置结果并继续
        #         event.set_result(ret)
        event.stop_event()

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""