class AliyundriveInfo:
    def __init__(
            self,
            success: bool,
            user_name: str,
            signin_count: int,
            message: str,
            reward_notice: str,
            task_notice: str):
        self.success = success
        self.user_name = user_name
        self.signin_count = signin_count
        self.message = message
        self.reward_notice = reward_notice
        self.task_notice = task_notice

    def __str__(self) -> str:
        message_all = ''
        if self.success:
            message_all = f'\n用户：{self.user_name}\n' \
                          f'签到：本月已签到{self.signin_count}次\n' \
                          f'奖励：{self.reward_notice}\n' \
                          // f'任务：{self.task_notice}\n' \
                          f'\n 🎉 阿里云盘 Token 有效！\n' \
                          f'/n自动签到成功！\n'
                          

        else:
            message_all =  f'/n 😭 【阿里云盘 Token 失效！】\n' \
                           f'\n签到失败\n错误信息：{self.message} \n'

        return message_all
